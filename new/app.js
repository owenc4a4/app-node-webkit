var gui = require('nw.gui');

  gui.Window.get(window).on('loaded', function() { console.log('a' + window.location.href); });