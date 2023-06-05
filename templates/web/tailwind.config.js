// /** @type {import('tailwindcss').Config} */
// module.exports = {
//   content: ["../html"],
//   theme: {
//     extend: {},
//   },
//   plugins: [],
// }

const path = require('path');

module.exports = {
  content: [
    path.join('templates/web/html/**/*.html'),
    path.join('templates/web/css/**/*.{html,js}'),
  ],
  theme: {
    extend: {},
  },
  plugins: [dev],
};
