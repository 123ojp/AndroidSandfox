Java.perform(function() {
  var SharedPreferencesImpl = Java.use("android.app.SharedPreferencesImpl");
  var SharedPreferencesImpl_EditorImpl = Java.use("android.app.SharedPreferencesImpl$EditorImpl");
  
  SharedPreferencesImpl.contains.implementation = function(key) {
    var value = this.contains.apply(this, arguments);
    var send_data = {};
    send_data.type = 'frida-SharedPreferences-contains'
    send_data.data = {
        'key':key ? key.toString() : 'null',
        'value': value ? value.toString() : 'null',

    }
    send(send_data);
    return value;
  };

  SharedPreferencesImpl.getInt.implementation = function(key, defValue) {
    var value = this.getInt.apply(this, arguments);
    var send_data = {};
    send_data.type = 'frida-SharedPreferences-getInt'
    send_data.data = {
        'key':key ? key.toString() : 'null',
        'value': value ? value.toString() : 'null',

    }
    send(send_data);
    return value;
  };

  SharedPreferencesImpl.getFloat.implementation = function(key, defValue) {

    var value = this.getFloat.apply(this, arguments);
    var send_data = {};
    send_data.type = 'frida-SharedPreferences-getFloat'
    send_data.data = {
        'key':key ? key.toString() : 'null',
        'value': value ? value.toString() : 'null',

    }
    send(send_data);
    return value;
  };

  SharedPreferencesImpl.getLong.implementation = function(key, defValue) {
    var value = this.getLong.apply(this, arguments);
    var send_data = {};
    send_data.type = 'frida-SharedPreferences-getLong'
    send_data.data = {
        'key':key ? key.toString() : 'null',
        'value': value ? value.toString() : 'null',

    }
    send(send_data);
    return value;
  };

  SharedPreferencesImpl.getBoolean.implementation = function(key, defValue) {

    var value = this.getBoolean.apply(this, arguments);

    var send_data = {};
    send_data.type = 'frida-SharedPreferences-getBoolean'
    send_data.data = {
        'key':key ? key.toString() : 'null',
        'value': value ? value.toString() : 'null',
    }
    send(send_data);
    return value;
  };

  SharedPreferencesImpl.getString.implementation = function(key, defValue) {
    var value = this.getString.apply(this, arguments);

    var send_data = {};
    send_data.type = 'frida-SharedPreferences-getString'
    send_data.data = {
        'key':key ? key.toString() : 'null',
        'value': value ? value.toString() : 'null',
    }
    send(send_data);
    return value;
  };

  SharedPreferencesImpl.getStringSet.implementation = function(key, defValue) {
    var value = this.getStringSet.apply(this, arguments);

    var send_data = {};
    send_data.type = 'frida-SharedPreferences-getStringSet'
    send_data.data = {
        'key':key ? key.toString() : 'null',
        'value': value ? value.toString() : 'null',
    }
    send(send_data);
    return value;
  };

  SharedPreferencesImpl_EditorImpl.putString.implementation = function(key, value) {
    var send_data = {};
    send_data.type = 'frida-SharedPreferences-putString'
    send_data.data = {
        'key':key ? key.toString() : 'null',
        'value': value ? value.toString() : 'null',
    }
    send(send_data);
    return this.putString.apply(this, arguments);
  };

  SharedPreferencesImpl_EditorImpl.putStringSet.implementation = function(key, values) {
    
    var send_data = {};
    send_data.type = 'frida-SharedPreferences-putStringSet'
    send_data.data = {
        'key':key ? key.toString() : 'null',
        'value': value ? value.toString() : 'null',
    }
    send(send_data);
    return this.putStringSet.apply(this, arguments);
  };

  SharedPreferencesImpl_EditorImpl.putInt.implementation = function(key, value) {
    
    var send_data = {};
    send_data.type = 'frida-SharedPreferences-putInt'
    send_data.data = {
        'key':key ? key.toString() : 'null',
        'value': value ? value.toString() : 'null',
    }
    send(send_data);
    return this.putInt.apply(this, arguments);
  };

  SharedPreferencesImpl_EditorImpl.putFloat.implementation = function(key, value) {
    
    var send_data = {};
    send_data.type = 'frida-SharedPreferences-putFloat'
    send_data.data = {
        'key':key ? key.toString() : 'null',
        'value': value ? value.toString() : 'null',
    }
    send(send_data);
    return this.putFloat.apply(this, arguments);
  };

  SharedPreferencesImpl_EditorImpl.putBoolean.implementation = function(key, value) {
    var send_data = {};
    send_data.type = 'frida-SharedPreferences-putBoolean'
    send_data.data = {
        'key':key ? key.toString() : 'null',
        'value': value ? value.toString() : 'null',
    }
    send(send_data);
    return this.putBoolean.apply(this, arguments);
  };

  SharedPreferencesImpl_EditorImpl.putLong.implementation = function(key, value) {
    var send_data = {};
    send_data.type = 'frida-SharedPreferences-putLong'
    send_data.data = {
        'key':key ? key.toString() : 'null',
        'value': value ? value.toString() : 'null',
    }
    send(send_data);
    return this.putLong.apply(this, arguments);
  };

  SharedPreferencesImpl_EditorImpl.remove.implementation = function(key) {
    var send_data = {};
    send_data.type = 'frida-SharedPreferences-remove'
    send_data.data = {
        'key':key ? key.toString() : 'null',
    }
    send(send_data);
    return this.remove.apply(this, arguments);
  };
});