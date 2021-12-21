function solve() {
    const URL = 'http://localhost:3030/jsonstore/collections/students';
    const nameRegex = /^[a-z]+$/i;

    const formEl = document.getElementById('form');
    const submitButton = document.getElementById('submit');

    const firstNameInput = document.querySelector('input[name="firstName"]');
    const lastNameInput = document.querySelector('input[name="lastName"]');
    const facultyNumberInput = document.querySelector('input[name="facultyNumber"]');
    const gradeInput = document.querySelector('input[name="grade"]');

    const tableBody = document.querySelector('#results tbody');

    const loadingEl = newEl('p', {}, 'Loading...');
    const submitResultEl = newEl('p');
    const studentCreationRulesEl = newEl('ul',
        {
            id: 'rules',
            style: "display: none;"
        },
        newEl('li', {}, 'FirstName: letters-only, non-empty'),
        newEl('li', {}, 'LastName: letters-only, non-empty'),
        newEl('li', {}, 'FacultyNumber: number, non-empty'),
        newEl('li', {}, 'Grade: number, non-empty')
    );

    formEl.appendChild(submitResultEl);
    formEl.appendChild(studentCreationRulesEl);

    showStudents();

    function showStudents() {
        tableBody.replaceChildren(loadingEl);

        extractStudents()
            .then(students => {
                let rows = [];
                students.forEach(student => {
                    const newRow = newEl('tr', {},
                        newEl('td', {}, student.firstName),
                        newEl('td', {}, student.lastName),
                        newEl('td', {}, student.facultyNumber),
                        newEl('td', {}, student.grade.toFixed(2)),
                    );
                    rows.push(newRow);

                });
                tableBody.replaceChildren(...rows);
            })
            .catch(error => {
                tableBody.replaceChildren(newEl('p', {}, 'Error: ' + error.message));
            });
    }

    async function extractStudents() {
        const response = await fetch(URL);
        const students = await response.json();

        return Object.values(students);
    }

    formEl.addEventListener('submit', event => {
        event.preventDefault();
        submitButton.disabled = true;

        const firstName = firstNameInput.value.trim();
        const lastName = lastNameInput.value.trim();
        const facultyNumber = facultyNumberInput.value.trim();
        let grade = gradeInput.value.trim();

        clearInputs();

        if (areInputsValid(firstName, lastName, facultyNumber, grade)) {
            studentCreationRulesEl.style.display = 'none';
            submitResultEl.textContent = 'Creating...';

            grade = +grade;

            createStudent({ firstName, lastName, facultyNumber, grade })
                .then(student => {
                    showStudents();
                    const message = `${student.firstName} ${student.lastName}: Successfully created!`;
                    submitResultEl.textContent = message;
                    submitButton.disabled = false;
                })
                .catch(error => {
                    submitResultEl.textContent = 'Error: ' + error.message;
                    submitButton.disabled = false;
                });
        } else {
            submitResultEl.textContent = 'Invalid input/s';
            studentCreationRulesEl.style.display = 'block';
            submitButton.disabled = false;
        };
    });

    function areInputsValid(firstName, lastName, facultyNumber, grade) {

        if (!(nameRegex.test(firstName))) return;
        if (!(nameRegex.test(lastName))) return;
        if (facultyNumber === '' || (!Number.isInteger(+facultyNumber))) return;
        if (grade === '' || Number.isNaN(+grade)) return;

        return true;
    }

    async function createStudent(studentData) {

        const options = {
            method: 'post',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(studentData)
        };

        const response = await fetch(URL, options);
        const responseBody = await response.json();

        return responseBody;
    }

    function clearInputs() {
        firstNameInput.value = '';
        lastNameInput.value = '';
        facultyNumberInput.value = '';
        gradeInput.value = '';
    }

    function newEl(type, attr, ...content) {
        const element = document.createElement(type);

        for (const prop in attr) {
            if (prop === 'class') {
                let classes = attr[prop].split(' ');
                for (let cls of classes) {
                    element.classList.add(cls);
                }
            } else {
                element.setAttribute(prop, attr[prop]);
            }
        }

        for (let item of content) {
            if (typeof item === 'string' || typeof item === 'number') {
                item = document.createTextNode(item);
            }

            element.appendChild(item);
        }

        return element;
    }
}

solve();