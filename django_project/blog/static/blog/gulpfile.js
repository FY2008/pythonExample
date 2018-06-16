var gulp = require('gulp');
var browserSync = require('browser-sync').create();
var sass = require('gulp-sass');



gulp.task('serve', ['sass'], function () {

  // Browsersys
  browserSync.init({
    server: "./bootstrap"
  });

  gulp.watch('bootstrap/scss/*.scss', ['sass']);
  //gulp.watch('bootstrap/*.html').on('change', browserSync.reload);
});

// Compile sass into CSS & auto-inject into browsers
gulp.task('sass', function () {
  return gulp.src('bootstrap/scss/*.scss')
    .pipe(sass())
    .pipe(gulp.dest('bootstrap/css'))
    .pipe(browserSync.stream());
});

gulp.task('default', ['serve']);