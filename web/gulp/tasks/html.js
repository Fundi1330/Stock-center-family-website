import rigger from 'gulp-rigger';

export const html = () => {
    return app.gulp.src(app.path.src.html)
        // .pipe(fileinclude({
        //     prefix: '@@',
        //     basepath: '@file'
        // }))
        .pipe(app.plugins.replace(/@img\//g, 'images/'))
        .pipe(rigger())
        .pipe(app.gulp.dest(`${app.path.build.html}`));
}