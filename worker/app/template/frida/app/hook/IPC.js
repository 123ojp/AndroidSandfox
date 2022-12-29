Java.perform(function () {
    var ContextWrapper = Java.use("android.content.ContextWrapper");

    if (ContextWrapper.sendBroadcast) {
        ContextWrapper.sendBroadcast.overload("android.content.Intent").implementation = function (intent) {
            var send_data = {};
            send_data.type = 'frida-IPC-Broadcast-Sent'
            send_data.data = {
                'intent': intent.toString(),
                'intent_extras': intent ? intent.getExtras() ? intent.getExtras().toString() : "null" : "null",
            }
            send(send_data);
            return this.sendBroadcast.overload("android.content.Intent").apply(this, arguments);
        };
        ContextWrapper.sendBroadcast.overload("android.content.Intent", "java.lang.String").implementation = function (intent, receiverPermission) {
            var send_data = {};
            send_data.type = 'frida-IPC-Broadcast-Sent'
            send_data.data = {
                'intent': intent.toString(),
                'intent_extras': intent ? intent.getExtras() ? intent.getExtras().toString() : "null" : "null",
            }
            send(send_data);
            return this.sendBroadcast.overload("android.content.Intent", "java.lang.String").apply(this, arguments);
        };
    }

    if (ContextWrapper.sendStickyBroadcast) {
        ContextWrapper.sendStickyBroadcast.overload("android.content.Intent").implementation = function (intent) {
            var send_data = {};
            send_data.type = 'frida-IPC-Broadcast-Sent'
            send_data.data = {
                'intent': intent.toString(),
                'intent_extras': intent ? intent.getExtras() ? intent.getExtras().toString() : "null" : "null",
            }
            send(send_data);
            return this.sendStickyBroadcast.overload("android.content.Intent").apply(this, arguments);
        };
    }

    if (ContextWrapper.startActivity) {
        ContextWrapper.startActivity.overload("android.content.Intent").implementation = function (intent) {
            var send_data = {};
            send_data.type = 'frida-IPC-Start-Activity'
            send_data.data = {
                'intent': intent.toString(),
            }
            send(send_data);
            return this.startActivity.overload("android.content.Intent").apply(this, arguments);
        };

        ContextWrapper.startActivity.overload("android.content.Intent", "android.os.Bundle").implementation = function (intent, bundle) {
            var send_data = {};
            send_data.type = 'frida-IPC-Start-Activity'
            send_data.data = {
                'intent': intent.toString(),
                'bundle': bundle.toString(),
            }
            send(send_data);
            return this.startActivity.overload("android.content.Intent", "android.os.Bundle").apply(this, arguments);
        };
    }

    if (ContextWrapper.startService) {
        ContextWrapper.startService.implementation = function (service) {
            var send_data = {};
            send_data.type = 'frida-IPC-Start-Service'
            send_data.data = {
                'service': service.toUri(0).toString(),
            }
            send(send_data);
            return this.startService.apply(this, arguments);
        };
    }

    if (ContextWrapper.stopService) {
        ContextWrapper.stopService.implementation = function (name) {
            var send_data = {};
            send_data.type = 'frida-IPC-stop-service'
            send_data.data = {
                'service': service.toUri(0).toString(),
            }
            send(send_data)
            return this.stopService.apply(this, arguments);
        };
    }

    if (ContextWrapper.registerReceiver) {
        ContextWrapper.registerReceiver.overload("android.content.BroadcastReceiver", "android.content.IntentFilter").implementation = function (receiver, filter) {
            return this.registerReceiver.apply(this, arguments);
        };
        ContextWrapper.registerReceiver.overload("android.content.BroadcastReceiver", "android.content.IntentFilter", "java.lang.String", "android.os.Handler").implementation = function (receiver, filter, broadcastPermission, scheduler) {
            return this.registerReceiver.apply(this, arguments);
        };
    }
});