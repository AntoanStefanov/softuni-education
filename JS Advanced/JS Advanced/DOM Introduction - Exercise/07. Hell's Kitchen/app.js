function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick() {
      let inputs = document.getElementById('inputs');
      let textArea = inputs.getElementsByTagName('textarea')[0];
      let data = textArea.value;
      let restaurantsData = JSON.parse(data);
      let restaurants = {};

      for (let restaurantInfo of restaurantsData) {
         let [restaurant, workersInfo] = restaurantInfo.split(' - ');

         if (!(restaurant in restaurants)) {
            restaurants[restaurant] = {};
            restaurants[restaurant]["workers"] = [];
            restaurants[restaurant].getAverageSalary = function () {
               let totalSalary = 0;
               let employees = restaurants[restaurant].workers.length;
               for (let workerInfo of restaurants[restaurant].workers) {
                  totalSalary += workerInfo[1];
               }
               return totalSalary / employees;
            }

            restaurants[restaurant].getBestSalary = function () {
               let bestSalary;
               for (let workerInfo of restaurants[restaurant].workers) {
                  if (workerInfo[1] > bestSalary || bestSalary === undefined) {
                     bestSalary = workerInfo[1];
                  }
               }
               return bestSalary;
            }
         }

         workersInfo = workersInfo.split(', ');

         for (let workerInfo of workersInfo) {
            let [worker, salary] = workerInfo.split(' ');
            salary = + salary;
            restaurants[restaurant]["workers"].push([worker, salary]);
         }
      }

      let bestSalary;
      let bestRestaurantName;
      for (let [name, info] of Object.entries(restaurants)) {
         let currentBestSalary = info.getAverageSalary();
         if (currentBestSalary > bestSalary || bestSalary === undefined) {
            bestSalary = currentBestSalary;
            bestRestaurantName = name;
         }
      }
      let bestRestaurantEl = document.getElementById('bestRestaurant');
      let paragraphRestaurantEl = bestRestaurantEl.getElementsByTagName('p')[0];
      paragraphRestaurantEl.textContent = `Name: ${bestRestaurantName} Average Salary: ${restaurants[bestRestaurantName].getAverageSalary().toFixed(2)} Best Salary: ${restaurants[bestRestaurantName].getBestSalary().toFixed(2)}`;

      let workers = restaurants[bestRestaurantName].workers;
      workers.sort((a, b) => b[1] - a[1]);
      let workersText = [];
      for (let worker of workers) {
         workersText.push(`Name: ${worker[0]} With Salary: ${worker[1]}`);
      }

      let workersEl = document.getElementById('workers');
      let paragraphWorkersEl = workersEl.getElementsByTagName('p')[0];
      paragraphWorkersEl.textContent = workersText.join(' ');
   }
}