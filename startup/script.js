var path = require('path');
var os = require('os');
var fs = require('fs');
var cp = require('child_process');
var exec = cp.exec;
var sqawn = cp.sqawn;

var required_file_win = [
   'ffmpegsumo.dll',
   'icudt.dll',
   'libEGL.dll',
   'libGLESv2.dll',
   'nw.exe',
   'nw.pak'
];
var source_file = ['index.html', 'package.json'];

var required_file = required_file_win;

var exec_root = path.dirname(process.execPath);

function copyExecFiles() {
  fs.mkdir('tmp');
  for (var i in required_file) {
    var src_file = path.join(exec_root, required_file[i]);
    var dst_file = path.join('tmp', required_file[i]);
    fs.createReadStream(src_file).pipe(fs.createWriteStream(dst_file));
  }
  
}

exports.copySourceFiles = function() {
  fs.createReadStream('../helloWorld/index.html').pipe(fs.createWriteStream('tmp/index.html'));
  fs.createReadStream('../helloWorld/package.json').pipe(fs.createWriteStream('tmp/package.json'));
}

exports.zipSourceFiles = function() {
  exec('python zip.py');
}

exports.makeExecuableFile = function() {
  if (os.platform() == 'win32') {
    exec('pak.bat');
  }
}
exports.copyExecFiles = copyExecFiles;