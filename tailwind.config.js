/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./website/templates/**/*.html",
    "./website/static/src/**/*.js",
    "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("flowbite/plugin")
  ],
}

