function solve(data, criteria) {
  let employees = JSON.parse(data);
  let filteredEmployees;
  if (criteria === 'all') {
    filteredEmployees = employees;
  } else {
    let [key, value] = criteria.split('-');
    filteredEmployees = employees.filter(function (employee) {
      if (key in employee) {
        return employee[key] === value;
      }
    })
  }
  let employeeNum = 0;
  for (let employee of filteredEmployees) {
    console.log(`${employeeNum}. ${employee.first_name} ${employee.last_name} - ${employee.email}`);
    employeeNum++;
  }
}

function solve(string, criteria) {
  let data;
  let propName, propValue;
  const isNotAll = criteria !== 'all';
  if (isNotAll) {
    [propName, propValue] = criteria.split('-');
    if (!propName || !propValue) {
      throw new Error('Invalid criteria');
    }
  }

  try {
    data = JSON.parse(string);
  } catch {
    data = [];
  }

  data.filter(function (i) {
    return isNotAll ? i[propName] === propValue : true;
  }).forEach((item, i) => {
    console.log(`${i}. ${item.first_name} ${item.last_name} - ${item.email}`);
  });
}

solve(`[{
    "id": "1",
    "first_name": "Ardine",
    "last_name": "Bassam",
    "email": "abassam0@cnn.com",
    "gender": "Female"
  }, {
    "id": "2",
    "first_name": "Kizzee",
    "last_name": "Jost",
    "email": "kjost1@forbes.com",
    "gender": "Female"
  },  
{
    "id": "3",
    "first_name": "Evanne",
    "last_name": "Maldin",
    "email": "emaldin2@hostgator.com",
    "gender": "Male"
  }]`,
  'non-Female',
)

solve(`[{
    "id": "1",
    "first_name": "Ardine",
    "last_name": "Bassam",
    "email": "abassam0@cnn.com",
    "gender": "Female"
  }, {
    "id": "2",
    "first_name": "Kizzee",
    "last_name": "Jost",
    "email": "kjost1@forbes.com",
    "gender": "Female"
  },  
{
    "id": "3",
    "first_name": "Evanne",
    "last_name": "Maldin",
    "email": "emaldin2@hostgator.com",
    "gender": "Male"
  }]`,
  'gender-Female',
)

solve(`[{
    "id": "1",
    "first_name": "Kaylee",
    "last_name": "Johnson",
    "email": "k0@cnn.com",
    "gender": "Female"
  }, {
    "id": "2",
    "first_name": "Kizzee",
    "last_name": "Johnson",
    "email": "kjost1@forbes.com",
    "gender": "Female"
  }, {
    "id": "3",
    "first_name": "Evanne",
    "last_name": "Maldin",
    "email": "emaldin2@hostgator.com",
    "gender": "Male"
  }, {
    "id": "4",
    "first_name": "Evanne",
    "last_name": "Johnson",
    "email": "ev2@hostgator.com",
    "gender": "Male"
  }]`,
  'last_name-Johnson')