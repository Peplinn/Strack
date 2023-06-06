// const searchField = document.querySelector("#searchField");
// const tableOutput = document.querySelector(".table-output");
// const appTable = document.querySelector(".app-table");
// const paginationContainer = document.querySelector(".pagination-container");
// const tbody = document.querySelector('.table-body');

// let debounceTimer;
// let currentSearchValue = ""; // Track the current search value

// tableOutput.style.display = "none";

// searchField.addEventListener('keyup', (e) => {
//     clearTimeout(debounceTimer);

//     const searchValue = e.target.value;

//     debounceTimer = setTimeout(() => {
//         if (searchValue.trim().length > 0) {
//             paginationContainer.style.display = "none";
//             console.log('searchValue', searchValue);

//             if (searchValue === currentSearchValue) {
//                 return; // Avoid duplicate requests for the same search value
//             }

//             currentSearchValue = searchValue;

//             fetch("/search-expense", {
//                 body: JSON.stringify({ searchText: searchValue }),
//                 method: "POST",
//             })
//             .then((res) => res.json())
//             .then((data) => {
//                 console.log("data", data);
//                 appTable.style.display = 'none';

//                 if (searchValue === currentSearchValue) {
//                     // Display the search results only if the current search value matches the latest query
//                     tableOutput.style.display = "block";

//                     if (data.length === 0) {
//                         tableOutput.innerHTML = "No results found.";
//                     } else {
//                         tbody.innerHTML = ""; // Clear the existing table rows
//                         data.forEach((item) => {
//                             tbody.innerHTML += `
//                                 <tr>
//                                     <td>${item.amount}</td>
//                                     <td>${item.description}</td>
//                                     <td>${item.category}</td>
//                                     <td>${item.date}</td>
//                                 </tr>
//                             `;
//                         });
//                     }
//                 }
//             });

//         } else {
//             currentSearchValue = ""; // Reset the current search value
//             tableOutput.style.display = "none";
//             appTable.style.display = 'block';
//             paginationContainer.style.display = "block";
//         }
//     }, 300); // Adjust the debounce delay (in milliseconds) as per your requirements
// });



// const searchField = document.querySelector("#searchField");

// const tableOutput = document.querySelector(".table-output");
// const appTable = document.querySelector(".app-table");
// const paginationContainer = document.querySelector(".pagination-container");
// tableOutput.style.display = "none";
// const noResults = document.querySelector(".no-results");
// const tbody = document.querySelector(".table-body");

// searchField.addEventListener("keyup", (e) => {
//   const searchValue = e.target.value;

//   if (searchValue.trim().length > 0) {
//     paginationContainer.style.display = "none";
//     tbody.innerHTML = "";
//     fetch("/search-expense", {
//       body: JSON.stringify({ searchText: searchValue }),
//       method: "POST",
//     })
//       .then((res) => res.json())
//       .then((data) => {
//         console.log("data", data);
//         appTable.style.display = "none";
//         tableOutput.style.display = "block";

//         console.log("data.length", data.length);

//         if (data.length === 0) {
//           noResults.style.display = "block";
//           tableOutput.style.display = "none";
//         } else {
//           noResults.style.display = "none";
//           data.forEach((item) => {
//             tbody.innerHTML += `
//                 <tr>
//                 <td>${item.amount}</td>
//                 <td>${item.category}</td>
//                 <td>${item.description}</td>
//                 <td>${item.date}</td>
//                 </tr>`;
//           });
//         }
//       });
//   } else {
//     tableOutput.style.display = "none";
//     appTable.style.display = "block";
//     paginationContainer.style.display = "block";
//   }
// });

const searchField = document.querySelector("#searchField");
const tableOutput = document.querySelector(".table-output");
const appTable = document.querySelector(".app-table");
const paginationContainer = document.querySelector(".pagination-container");
const noResults = document.querySelector(".no-results");
const tbody = document.querySelector(".table-body");

let debounceTimer;

tableOutput.style.display = "none";
noResults.style.display = "none";

searchField.addEventListener("keyup", (e) => {
  clearTimeout(debounceTimer);

  const searchValue = e.target.value;

  debounceTimer = setTimeout(() => {
    if (searchValue.trim().length > 0) {
      paginationContainer.style.display = "none";
      tbody.innerHTML = "";

      fetch("/search-expense", {
        body: JSON.stringify({ searchText: searchValue }),
        method: "POST",
      })
        .then((res) => res.json())
        .then((data) => {
          console.log("data", data);
          appTable.style.display = "none";
          tableOutput.style.display = "block";

          if (data.length === 0) {
            noResults.style.display = "block";
            tableOutput.style.display = "none";
          } else {
            noResults.style.display = "none";
            data.forEach((item) => {
              tbody.innerHTML += `
                  <tr>
                  <td>${item.amount}</td>
                  <td>${item.category}</td>
                  <td>${item.description}</td>
                  <td>${item.date}</td>
                  </tr>`;
            });
          }
        });
    } else {
      tableOutput.style.display = "none";
      appTable.style.display = "block";
      paginationContainer.style.display = "block";
    }
  }, 300); // Adjust the debounce delay (in milliseconds) as per your requirements
});
