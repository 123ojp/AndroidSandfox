// class created from
// struct JNINativeInterface :
// https://android.googlesource.com/platform/libnativehelper/+/master/include_jni/jni.h#129
// https://github.com/Areizen/JNI-Frida-Hook
const jni_struct_array = [
    "reserved0",
    "reserved1",
    "reserved2",
    "reserved3",
    "GetVersion",
    "DefineClass",
    "FindClass",
    "FromReflectedMethod",
    "FromReflectedField",
    "ToReflectedMethod",
    "GetSuperclass",
    "IsAssignableFrom",
    "ToReflectedField",
    "Throw",
    "ThrowNew",
    "ExceptionOccurred",
    "ExceptionDescribe",
    "ExceptionClear",
    "FatalError",
    "PushLocalFrame",
    "PopLocalFrame",
    "NewGlobalRef",
    "DeleteGlobalRef",
    "DeleteLocalRef",
    "IsSameObject",
    "NewLocalRef",
    "EnsureLocalCapacity",
    "AllocObject",
    "NewObject",
    "NewObjectV",
    "NewObjectA",
    "GetObjectClass",
    "IsInstanceOf",
    "GetMethodID",
    "CallObjectMethod",
    "CallObjectMethodV",
    "CallObjectMethodA",
    "CallBooleanMethod",
    "CallBooleanMethodV",
    "CallBooleanMethodA",
    "CallByteMethod",
    "CallByteMethodV",
    "CallByteMethodA",
    "CallCharMethod",
    "CallCharMethodV",
    "CallCharMethodA",
    "CallShortMethod",
    "CallShortMethodV",
    "CallShortMethodA",
    "CallIntMethod",
    "CallIntMethodV",
    "CallIntMethodA",
    "CallLongMethod",
    "CallLongMethodV",
    "CallLongMethodA",
    "CallFloatMethod",
    "CallFloatMethodV",
    "CallFloatMethodA",
    "CallDoubleMethod",
    "CallDoubleMethodV",
    "CallDoubleMethodA",
    "CallVoidMethod",
    "CallVoidMethodV",
    "CallVoidMethodA",
    "CallNonvirtualObjectMethod",
    "CallNonvirtualObjectMethodV",
    "CallNonvirtualObjectMethodA",
    "CallNonvirtualBooleanMethod",
    "CallNonvirtualBooleanMethodV",
    "CallNonvirtualBooleanMethodA",
    "CallNonvirtualByteMethod",
    "CallNonvirtualByteMethodV",
    "CallNonvirtualByteMethodA",
    "CallNonvirtualCharMethod",
    "CallNonvirtualCharMethodV",
    "CallNonvirtualCharMethodA",
    "CallNonvirtualShortMethod",
    "CallNonvirtualShortMethodV",
    "CallNonvirtualShortMethodA",
    "CallNonvirtualIntMethod",
    "CallNonvirtualIntMethodV",
    "CallNonvirtualIntMethodA",
    "CallNonvirtualLongMethod",
    "CallNonvirtualLongMethodV",
    "CallNonvirtualLongMethodA",
    "CallNonvirtualFloatMethod",
    "CallNonvirtualFloatMethodV",
    "CallNonvirtualFloatMethodA",
    "CallNonvirtualDoubleMethod",
    "CallNonvirtualDoubleMethodV",
    "CallNonvirtualDoubleMethodA",
    "CallNonvirtualVoidMethod",
    "CallNonvirtualVoidMethodV",
    "CallNonvirtualVoidMethodA",
    "GetFieldID",
    "GetObjectField",
    "GetBooleanField",
    "GetByteField",
    "GetCharField",
    "GetShortField",
    "GetIntField",
    "GetLongField",
    "GetFloatField",
    "GetDoubleField",
    "SetObjectField",
    "SetBooleanField",
    "SetByteField",
    "SetCharField",
    "SetShortField",
    "SetIntField",
    "SetLongField",
    "SetFloatField",
    "SetDoubleField",
    "GetStaticMethodID",
    "CallStaticObjectMethod",
    "CallStaticObjectMethodV",
    "CallStaticObjectMethodA",
    "CallStaticBooleanMethod",
    "CallStaticBooleanMethodV",
    "CallStaticBooleanMethodA",
    "CallStaticByteMethod",
    "CallStaticByteMethodV",
    "CallStaticByteMethodA",
    "CallStaticCharMethod",
    "CallStaticCharMethodV",
    "CallStaticCharMethodA",
    "CallStaticShortMethod",
    "CallStaticShortMethodV",
    "CallStaticShortMethodA",
    "CallStaticIntMethod",
    "CallStaticIntMethodV",
    "CallStaticIntMethodA",
    "CallStaticLongMethod",
    "CallStaticLongMethodV",
    "CallStaticLongMethodA",
    "CallStaticFloatMethod",
    "CallStaticFloatMethodV",
    "CallStaticFloatMethodA",
    "CallStaticDoubleMethod",
    "CallStaticDoubleMethodV",
    "CallStaticDoubleMethodA",
    "CallStaticVoidMethod",
    "CallStaticVoidMethodV",
    "CallStaticVoidMethodA",
    "GetStaticFieldID",
    "GetStaticObjectField",
    "GetStaticBooleanField",
    "GetStaticByteField",
    "GetStaticCharField",
    "GetStaticShortField",
    "GetStaticIntField",
    "GetStaticLongField",
    "GetStaticFloatField",
    "GetStaticDoubleField",
    "SetStaticObjectField",
    "SetStaticBooleanField",
    "SetStaticByteField",
    "SetStaticCharField",
    "SetStaticShortField",
    "SetStaticIntField",
    "SetStaticLongField",
    "SetStaticFloatField",
    "SetStaticDoubleField",
    "NewString",
    "GetStringLength",
    "GetStringChars",
    "ReleaseStringChars",
    "NewStringUTF",
    "GetStringUTFLength",
    "GetStringUTFChars",
    "ReleaseStringUTFChars",
    "GetArrayLength",
    "NewObjectArray",
    "GetObjectArrayElement",
    "SetObjectArrayElement",
    "NewBooleanArray",
    "NewByteArray",
    "NewCharArray",
    "NewShortArray",
    "NewIntArray",
    "NewLongArray",
    "NewFloatArray",
    "NewDoubleArray",
    "GetBooleanArrayElements",
    "GetByteArrayElements",
    "GetCharArrayElements",
    "GetShortArrayElements",
    "GetIntArrayElements",
    "GetLongArrayElements",
    "GetFloatArrayElements",
    "GetDoubleArrayElements",
    "ReleaseBooleanArrayElements",
    "ReleaseByteArrayElements",
    "ReleaseCharArrayElements",
    "ReleaseShortArrayElements",
    "ReleaseIntArrayElements",
    "ReleaseLongArrayElements",
    "ReleaseFloatArrayElements",
    "ReleaseDoubleArrayElements",
    "GetBooleanArrayRegion",
    "GetByteArrayRegion",
    "GetCharArrayRegion",
    "GetShortArrayRegion",
    "GetIntArrayRegion",
    "GetLongArrayRegion",
    "GetFloatArrayRegion",
    "GetDoubleArrayRegion",
    "SetBooleanArrayRegion",
    "SetByteArrayRegion",
    "SetCharArrayRegion",
    "SetShortArrayRegion",
    "SetIntArrayRegion",
    "SetLongArrayRegion",
    "SetFloatArrayRegion",
    "SetDoubleArrayRegion",
    "RegisterNatives",
    "UnregisterNatives",
    "MonitorEnter",
    "MonitorExit",
    "GetJavaVM",
    "GetStringRegion",
    "GetStringUTFRegion",
    "GetPrimitiveArrayCritical",
    "ReleasePrimitiveArrayCritical",
    "GetStringCritical",
    "ReleaseStringCritical",
    "NewWeakGlobalRef",
    "DeleteWeakGlobalRef",
    "ExceptionCheck",
    "NewDirectByteBuffer",
    "GetDirectBufferAddress",
    "GetDirectBufferCapacity",
    "GetObjectRefType"
]


//Calculate the given funcName address from the JNIEnv pointer

function getJNIFunctionAddress(jnienv_addr, func_name) {
    var offset = jni_struct_array.indexOf(func_name) * Process.pointerSize

    // console.log("offset : 0x" + offset.toString(16))

    return Memory.readPointer(jnienv_addr.add(offset))
}

/*
// Hook all function to have an overview of the function called
function hook_all(jnienv_addr) {
    jni_struct_array.forEach(function (func_name) {
        // Calculating the address of the function
        if (!func_name.includes("reserved")) {
            var func_addr = getJNIFunctionAddress(jnienv_addr, func_name)
            Interceptor.attach(func_addr, {
                onEnter: function (args) {
                    console.log("[+] Entered : " + func_name)
                },
                onLeave: function (args) {
                    // Prevent from displaying junk from other functions

                }
            })
        }
    })
}*/

var hookedlist = []
var hook = ["NewStringUTF", "FindClass", "NewString"]

function hook_func(library_name) {
    // To get the list of exports
    Module.enumerateExportsSync(library_name).forEach(function (symbol) {

        if (symbol.name.includes("Java_")||symbol.name.includes("NewStringUTF")||
        symbol.name.includes("FindClass")||symbol.name.includes("NewString")) {
            console.log("[...] Hooking : " + library_name + " -> " + symbol.name + " at " + symbol.address)

            Interceptor.attach(symbol.address, {
                onEnter: function (args) {

                    var jnienv_addr = Memory.readPointer(args[0])

                    console.log("[+] Hooked successfully, JNIEnv base adress :" + jnienv_addr)
                    var func_symbol = DebugSymbol.fromAddress(this.context.pc)['name'];
                    if (hookedlist.includes(jnienv_addr)) {
                        return
                    } else {
                        hookedlist.push(jnienv_addr)
                        hook.forEach(function (symbol) {
                            Interceptor.attach(getJNIFunctionAddress(jnienv_addr, symbol), {
                                onEnter: function (args) {
                                    console.log(library_name + "->" + symbol + "(\"" + Memory.readCString(args[1]) + "\")")
                                    var send_data = {};
                                    send_data.type = 'frida-Native-'+symbol
                                    send_data.data = {
                                        'value':Memory.readCString(args[1]),
                                        'func':func_symbol,   
                                        'lib':library_name,
                                    }
                                    send(send_data);
                                }
                            })
                        })

                    }

                },
                onLeave: function (args) {

                }
            })
        }

    })
}

var hookpath;
Interceptor.attach(Module.findExportByName(null, 'android_dlopen_ext'), {
    onEnter: function (args) {
        var library_path = Memory.readCString(args[0])

        var send_data = {};
        send_data.type = 'frida-JNILib-Load'
        send_data.data = {
            'path': library_path,
        }
        send(send_data);
        hookpath = library_path
        console.log(hookpath)
    },
    onLeave: function (args) {
        if (hookpath.includes(".so") &&
            !hookpath.includes("/system/") &&
            !hookpath.includes("libwebviewchromium") &&
            !hookpath.includes("redroid") &&
            !hookpath.includes("/vendor/")
        ) {
            hookpath = hookpath.substring(hookpath.lastIndexOf('/') + 1)
            hook_func(hookpath)
        }
    }
})

Java.perform(function(){
    const System = Java.use('java.lang.System');
    const Runtime = Java.use('java.lang.Runtime');
    const SystemLoad_2 = System.loadLibrary.overload('java.lang.String');
    const VMStack = Java.use('dalvik.system.VMStack');

    SystemLoad_2.implementation = function(library) {
        console.log("Loading dynamic library => " + library);
        try {
            const loaded = Runtime.getRuntime().loadLibrary0(VMStack.getCallingClassLoader(), library);
            var library_path = 'lib'+library+'.so'
            var send_data = {};
            send_data.type = 'frida-JNILib-Load'
            send_data.data = {
                'path': library_path,
            }
            send(send_data);
            if (library_path.includes(".so") &&
                !library_path.includes("/system/") &&
                !library_path.includes("libwebviewchromium") &&
                !library_path.includes("redroid") &&
                !library_path.includes("/vendor/")
            ) {
                hook_func(library_path)
            }
            return loaded;
        } catch(e) {
            console.log(e);
        }
    };
});

