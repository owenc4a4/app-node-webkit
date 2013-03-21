console.log('ij');
global.pi = 'gooo';
var poo = exports.goo;
setInterval(function() {
  var win = exports.currentWindow;
  //console.log(poo);
  //console.log(global.pi);
  console.log('wa wa', win.window.location.href);
}, 2000);

