// grab our gulp packages
var gulp  = require('gulp'),
    gutil = require('gulp-util');
    sass = require('gulp-ruby-sass') 
    notify = require("gulp-notify") 
    bower = require('gulp-bower');

var config = {
     sassPath: './resources/sass',
     bowerDir: './bower_components' 
}

gulp.task('bower', function() { 
    return bower()
         .pipe(gulp.dest(config.bowerDir)) 
});

gulp.task('bootstrap', function() {
    return gulp.src(config.bowerDir + "/bootstrap/dist/**")
        .pipe(gulp.dest("./app/static/bootstrap"))
});

gulp.task('jquery', function() {
    return gulp.src(config.bowerDir + "/jquery/dist/**")
        .pipe(gulp.dest("./app/static/jquery"))
});

//gulp.task('default', ['bower', 'bootstrap', 'jquery']);
//bootstrap cez flask-bootstrap
gulp.task('default', ['bower']);
