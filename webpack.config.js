const path = require("path");

module.exports = {
  mode: "development",
  entry: "./UI/js/index.js",
  output: {
    path: path.resolve(__dirname, "UI/js"),
    filename: "main.js"
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /(node_modules)/,
        use: {
          loader: "babel-loader"
        }
      }
    ]
  }
};
