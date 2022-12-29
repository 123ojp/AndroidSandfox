// hook open syscall

Interceptor.attach(Module.getExportByName(null, 'open'), {
    onEnter: function (args) {
      send({
        type: 'open',
        path: Memory.readUtf8String(args[0])
      });
    }
  });
  Interceptor.attach(Module.getExportByName(null, 'fopen'), {
    onEnter: function (args) {
      send({
        type: 'open',
        path: Memory.readUtf8String(args[0])
      });
    }
  });

// hook file exit syscall
Interceptor.attach(Module.getExportByName(null, 'faccessat'), {
  onEnter: function (args) {
    send({
      type: 'frida-faccessat',
      path: Memory.readUtf8String(args[1]),
      data: {
        path:Memory.readUtf8String(args[1]),
        mode:args[2],
      },
    });
  }
});
Interceptor.attach(Module.getExportByName(null, 'fstatat64'), {
  onEnter: function (args) {
    send({
      type: 'frida-faccessat',
      path: Memory.readUtf8String(args[1]),
      data: {
        path:Memory.readUtf8String(args[1]),
        mode:args[2],
      },
    });
  }
});