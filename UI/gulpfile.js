const gulp = require("gulp");
const sourcemaps = require("gulp-sourcemaps");
const livereload = require("gulp-livereload");
const watch = require("gulp-watch");
const batch = require("gulp-batch");

// JavaScript development.
const browserify = require("browserify");
const babelify = require("babelify");
const source = require("vinyl-source-stream");
const buffer = require("vinyl-buffer");
const uglify = require("gulp-uglify");
const gutil = require("gulp-util");

// CSS compilation.
const concat = require("gulp-concat");
const cleanCSS = require("gulp-clean-css");

const clean = require("gulp-clean");

// Task clean build folder
gulp.task("clean", () => {
  gulp.src("build", { read: false }).pipe(clean());
});

// Task to compile js.
gulp.task("compile-js", () => {
  // app.js is your main JS file with all your module inclusions
  return browserify({
    entries: ["src/js/index.js"],
    debug: true
  })
    .transform(babelify, { presets: ["@babel/env"] })
    .on("error", gutil.log)
    .bundle()
    .on("error", gutil.log)
    .pipe(source("bundle.min.js"))
    .pipe(buffer())
    .pipe(sourcemaps.init())
    .pipe(uglify())
    .pipe(sourcemaps.write("./maps"))
    .pipe(gulp.dest("build/js"))
    .pipe(livereload());
});

// Task to minify css.
gulp.task("minify-css", () => {
  return gulp
    .src(["src/css/style.css"])
    .pipe(sourcemaps.init())
    .pipe(cleanCSS({ debug: true }))
    .pipe(concat("style.min.css"))
    .pipe(sourcemaps.write("./maps"))
    .pipe(gulp.dest("build/css"))
    .pipe(livereload());
});

// Task to copy images to build.
gulp.task("copy-images", () => {
  return gulp.src(["src/img/**/*"]).pipe(gulp.dest("build/img/"));
});

// Task to copy html to build.
gulp.task("copy-html", () => {
  return gulp.src(["public/*.html"]).pipe(gulp.dest("build/"));
});

// Task to copy fonts to build.
gulp.task("copy-fonts", () => {
  return gulp.src(["src/fonts/**/*"]).pipe(gulp.dest("build/fonts/"));
});

// Task to watch.
gulp.task("watch", () => {
  // Watch all js files recursively.
  watch(
    ["src/js/**/*"],
    batch((events, done) => {
      gulp.start(["compile-js"], done);
    })
  );

  // Watch all css files recursively.
  watch(
    ["src/css/**/*"],
    batch((events, done) => {
      gulp.start(["minify-css"], done);
    })
  );

  // Watch all html files recursively.
  watch(
    ["public/*.html"],
    batch((events, done) => {
      gulp.start(["copy-html"], done);
    })
  );

  // Watch all image files recursively.
  watch(
    ["src/img/**/*"],
    batch((events, done) => {
      gulp.start("copy-images", done);
    })
  );

  // Watch all font files recursively.
  watch(
    ["src/fonts/**/*"],
    batch((events, done) => {
      gulp.start("copy-fonts", done);
    })
  );
});

// Development:
// Task when running `gulp` from terminal.
gulp.task("default", ["build"]);

// Production:
// Task when running `gulp build` from terminal.
gulp.task("build", [
  "minify-css",
  "copy-images",
  "copy-fonts",
  "copy-html",
  "compile-js",
  "watch"
]);
