var byteArraytoHexString = function (byteArray) {
    if (byteArray && byteArray.map) {
        return byteArray.map(function (byte) {
            return ('0' + (byte & 0xFF).toString(16)).slice(-2);
        }).join('')
    } else {
        return byteArray + "";
    }
}

var normalize = function (input) {
    if (input.length && input.length > 0) {
        var normalized = byteArraytoHexString(input);
    } else if (input.array) {
        var normalized = byteArraytoHexString(input.array());
    } else {
        var normalized = input.toString();
    }
    return normalized;
}


var hexToAscii = function (input) {
    var hex = input.toString();
    var str = '';
    for (var i = 0; i < hex.length; i += 2)
        str += String.fromCharCode(parseInt(hex.substr(i, 2), 16));
    return str;
}

Java.perform(function () {
    var SQLiteDatabase = Java.use("android.database.sqlite.SQLiteDatabase");
    if (SQLiteDatabase.execSQL) {
        SQLiteDatabase.execSQL.overloads[0].implementation = function (sql) {

            var send_data = {};
            send_data.type = 'frida-SQLite-execSQL'
            send_data.data = {
                'sql_exec': sql ? sql.toString() : 'null',
            }
            send(send_data);
            return this.execSQL.overloads[0].apply(this, arguments);
        }

        SQLiteDatabase.execSQL.overloads[1].implementation = function (sql, bindArgs) {
            var send_data = {};
            send_data.type = 'frida-SQLite-execSQL'
            send_data.data = {
                'sql_exec': sql ? sql.toString() : 'null',
            }

            if (bindArgs) {
                send_data.data.bindArgs = bindArgs ? bindArgs.toString() : 'null';
            }
            send(send_data);
            return this.execSQL.overloads[1].apply(this, arguments);
        }
    }

    if (SQLiteDatabase.getPath) {
        SQLiteDatabase.getPath.implementation = function () {
            var dbPath = this.getPath.call(this);
            var send_data = {};
            send_data.type = 'frida-SQLite-getPath'
            send_data.data = {
                'db_path': dbPath ? dbPath.toString() : 'null'
            }
            send(send_data);
            return dbPath;
        }
    }
    if (SQLiteDatabase.insert) {
        SQLiteDatabase.insert.implementation = function (table, nullColumnHack, values) {
            var send_data = {};
            send_data.type = 'frida-SQLite-insert'
            send_data.data = {
                'table_name': table ? table.toString() : 'null',
            }
            if (values) {           
               send_data.data.value = values ? values.toString() : 'null';
            }
            send(send_data);
            return this.insert.apply(this, arguments);
        }
    }

    if (SQLiteDatabase.insertOrThrow) {
        SQLiteDatabase.insertOrThrow.implementation = function (table, nullColumnHack, values) {
            var send_data = {};
            send_data.type = 'frida-SQLite-insert'
            send_data.data = {
                'table_name': table ? table.toString() : 'null',
            }
            if (values) {           
               send_data.data.value = values ? values.toString() : 'null';
            }
            send(send_data);
            return this.insertOrThrow.apply(this, arguments);
        }
    }
    if (SQLiteDatabase.insertWithOnConflict) {
        SQLiteDatabase.insertWithOnConflict.implementation = function (table, nullColumnHack, values, conflictAlgorithm) {
            var send_data = {};
            send_data.type = 'frida-SQLite-insert'
            send_data.data = {
                'table_name': table ? table.toString() : 'null',
            }
            if (values) {           
               send_data.data.value = values ? values.toString() : 'null';
            }
            send(send_data);
            return this.insertWithOnConflict.apply(this, arguments);
        }
    }

    if (SQLiteDatabase.openDatabase) {
        SQLiteDatabase.openDatabase.overloads[0].implementation = function (path, factory, flags) {
            if (flags === SQLiteDatabase.OPEN_READWRITE) {
                flags = "OPEN_READWRITE";
            } else if (flags === SQLiteDatabase.OPEN_READONLY) {
                flags = "OPEN_READONLY";
            } else if (flags === SQLiteDatabase.CREATE_IF_NECESSARY) {
                flags = "CREATE_IF_NECESSARY";
            } else if (flags === SQLiteDatabase.NO_LOCALIZED_COLLATORS) {
                flags = "NO_LOCALIZED_COLLATORS";
            }
            var send_data = {};
            send_data.type = 'frida-SQLite-openDB'
            send_data.data = {
                'db_path': path ? path.toString() : 'null',
                'flag':flags,
            }
            send(send_data);
            return this.openDatabase.overloads[0].apply(this, arguments);
        }

        SQLiteDatabase.openDatabase.overloads[1].implementation = function (path, factory, flags, errorHandler) {
            if (flags === SQLiteDatabase.OPEN_READWRITE) {
                flags = "OPEN_READWRITE";
            } else if (flags === SQLiteDatabase.OPEN_READONLY) {
                flags = "OPEN_READONLY";
            } else if (flags === SQLiteDatabase.CREATE_IF_NECESSARY) {
                flags = "CREATE_IF_NECESSARY";
            } else if (flags === SQLiteDatabase.NO_LOCALIZED_COLLATORS) {
                flags = "NO_LOCALIZED_COLLATORS";
            }
            var send_data = {};
            send_data.type = 'frida-SQLite-openDB'
            send_data.data = {
                'db_path': path ? path.toString() : 'null',
                'flag':flags,
            }
            send(send_data);
            return this.openDatabase.overloads[1].apply(this, arguments);
        }
    }
    if (SQLiteDatabase.openOrCreateDatabase) {
        SQLiteDatabase.openOrCreateDatabase.overloads[0].implementation = function (file, factory) {
            if (file) {
                var send_data = {};
                send_data.type = 'frida-SQLite-openOrCreateDB'
                send_data.data = {
                    'db_path': file ? file.toString() : 'null',
                }
                send(send_data);
            }
            return this.openOrCreateDatabase.overloads[0].apply(this, arguments);
        }
        SQLiteDatabase.openOrCreateDatabase.overloads[1].implementation = function (file, factory, errorHandler) {
            if (file) {
                var send_data = {};
                send_data.type = 'frida-SQLite-openOrCreateDB'
                send_data.data = {
                    'db_path': file ? file.toString() : 'null',
                }
                send(send_data);
            }
            return this.openOrCreateDatabase.overloads[1].apply(this, arguments);
        }


        SQLiteDatabase.openOrCreateDatabase.overloads[2].implementation = function (file, factory) {
            var send_data = {};
            send_data.type = 'frida-SQLite-openOrCreateDB'
            send_data.data = {
                'db_path': file ? file.toString() : 'null',
            }
            send(send_data);
            return this.openOrCreateDatabase.overloads[2].apply(this, arguments);
        }
    }
    if (SQLiteDatabase.query) {
        SQLiteDatabase.query.overloads[0].implementation = function (distinct, table, columns, selection, selectionArgs, groupBy, having, orderBy, limit) {

            var send_data = {};
            send_data.type = 'frida-SQLite-query'
            send_data.data = {
                'distinct':distinct ? distinct.toString() : 'null',
                'table': table ? table.toString() : 'null',
                'columns': columns ? columns.toString() : 'null',

            }
            send(send_data);

            var Cursor = this.query.overloads[0].apply(this, arguments);
            var CursorCopy = Cursor;

            return CursorCopy;
        }
    }

    // Ref: https://developer.android.com/reference/android/database/sqlite/SQLiteDatabase.html#query(java.lang.String, java.lang.String[], java.lang.String, java.lang.String[], java.lang.String, java.lang.String, java.lang.String, java.lang.String)
    if (SQLiteDatabase.query) {
        SQLiteDatabase.query.overloads[1].implementation = function (table, columns, selection, selectionArgs, groupBy, having, orderBy, limit) {
            var send_data = {};
            send_data.type = 'frida-SQLite-query'
            send_data.data = {
                'table': table ? table.toString() : 'null',
                'columns': columns ? columns.toString() : 'null',

            }
            send(send_data);
            var Cursor = this.query.overloads[1].apply(this, arguments);
            var CursorCopy = Cursor;

            return CursorCopy;
        }
    }

    if (SQLiteDatabase.query) {
        SQLiteDatabase.query.overloads[2].implementation = function (distinct, table, columns, selection, selectionArgs, groupBy, having, orderBy, limit, cancellationSignal) {
            var send_data = {};
            send_data.type = 'frida-SQLite-query'
            send_data.data = {
                'distinct':distinct ? distinct.toString() : 'null',
                'table': table ? table.toString() : 'null',
                'columns': columns ? columns.toString() : 'null',

            }
            send(send_data);

            var Cursor = this.query.overloads[2].apply(this, arguments);
            var CursorCopy = Cursor;
            return CursorCopy;
        }
    }

    if (SQLiteDatabase.query) {
        SQLiteDatabase.query.overloads[3].implementation = function (table, columns, selection, selectionArgs, groupBy, having, orderBy) {
            var send_data = {};
            send_data.type = 'frida-SQLite-query'
            send_data.data = {
                'table': table ? table.toString() : 'null',
                'columns': columns ? columns.toString() : 'null',

            }
            send(send_data);
            var Cursor = this.query.overloads[3].apply(this, arguments);
            var CursorCopy = Cursor;
            return CursorCopy;
        }
    }

    if (SQLiteDatabase.queryWithFactory) {
        SQLiteDatabase.queryWithFactory.overloads[0].implementation = function (cursorFactory, distinct, table, columns, selection, selectionArgs, groupBy, having, orderBy, limit, cancellationSignal) {
            var send_data = {};
            send_data.type = 'frida-SQLite-query'
            send_data.data = {
                'distinct':distinct ? distinct.toString() : 'null',
                'table': table ? table.toString() : 'null',
                'columns': columns ? columns.toString() : 'null',

            }
            send(send_data);

            var Cursor = this.queryWithFactory.overloads[0].apply(this, arguments);
            var CursorCopy = Cursor;

            return CursorCopy;
        }
    }

    if (SQLiteDatabase.queryWithFactory) {
        SQLiteDatabase.queryWithFactory.overloads[1].implementation = function (cursorFactory, distinct, table, columns, selection, selectionArgs, groupBy, having, orderBy, limit) {
            var send_data = {};
            send_data.type = 'frida-SQLite-query'
            send_data.data = {
                'distinct':distinct ? distinct.toString() : 'null',
                'table': table ? table.toString() : 'null',
                'columns': columns ? columns.toString() : 'null',

            }
            send(send_data);
            var Cursor = this.queryWithFactory.overloads[1].apply(this, arguments);

            return Cursor;
        }
    }
    if (SQLiteDatabase.rawQuery) {
        SQLiteDatabase.rawQuery.overloads[0].implementation = function (sql, selectionArgs, cancellationSignal) {
            var send_data = {};
            send_data.type = 'frida-SQLite-rawQuery'
            send_data.data = {
                'sql':sql ? sql.toString() : 'null',

            }
            send(send_data);

            var Cursor = this.rawQuery.overloads[0].apply(this, arguments);
            var CursorCopy = Cursor;
            return CursorCopy;
        }
    }

    if (SQLiteDatabase.rawQuery) {

        SQLiteDatabase.rawQuery.overloads[1].implementation = function (sql, selectionArgs) {
            var send_data = {};
            send_data.type = 'frida-SQLite-rawQuery'
            send_data.data = {
                'sql':sql ? sql.toString() : 'null',

            }
            send(send_data);
            var Cursor = this.rawQuery.overloads[1].apply(this, arguments);
            var CursorCopy = Cursor;
            return CursorCopy;
        }
    }

    if (SQLiteDatabase.rawQueryWithFactory) {
        SQLiteDatabase.rawQueryWithFactory.overloads[0].implementation = function (cursorFactory, sql, selectionArgs, editTable, cancellationSignal) {
            var send_data = {};
            send_data.type = 'frida-SQLite-rawQuery'
            send_data.data = {
                'sql':sql ? sql.toString() : 'null',

            }
            send(send_data);
            var Cursor = this.rawQueryWithFactory.overloads[0].apply(this, arguments);
            var CursorCopy = Cursor;

        
            return CursorCopy;
        }
    }

    if (SQLiteDatabase.rawQueryWithFactory) {
        SQLiteDatabase.rawQueryWithFactory.overloads[1].implementation = function (cursorFactory, sql, selectionArgs, editTable) {
            var send_data = {};
            send_data.type = 'frida-SQLite-rawQuery'
            send_data.data = {
                'sql':sql ? sql.toString() : 'null',

            }
            send(send_data);

            var Cursor = this.rawQueryWithFactory.overloads[1].apply(this, arguments);
            var CursorCopy = Cursor;
            return CursorCopy;
        }
    }

    if (SQLiteDatabase.update) {
        SQLiteDatabase.update.implementation = function (table, values, whereClause, whereArgs) {
            var send_data = {};
            send_data.type = 'frida-SQLite-update'
            send_data.data = {
                'table':table ? table.toString() : 'null',
                'value':values ? values.toString() : 'null',

            }
            send(send_data);

            return this.update.apply(this, arguments);
        }
    }

    if (SQLiteDatabase.updateWithOnConflict) {
        SQLiteDatabase.updateWithOnConflict.implementation = function (table, values, whereClause, whereArgs, conflictAlgorithm) {
            var send_data = {};
            send_data.type = 'frida-SQLite-update'
            send_data.data = {
                'table':table ? table.toString() : 'null',
                'value':values ? values.toString() : 'null',

            }
            send(send_data);
            return this.updateWithOnConflict.apply(this, arguments);
        }
    }

    if (SQLiteDatabase.create) {
        SQLiteDatabase.create.implementation = function (factory) {
            var db = this.create.apply(this, arguments);
            var send_data = {};
            send_data.type = 'frida-SQLite-create'
            send_data.data = {
                'db_path':db.getPath() ? db.getPath().toString() : 'null',
            }
            send(send_data);
            return db;
        }
    }


    if (SQLiteDatabase.deleteDatabase) {
        SQLiteDatabase.deleteDatabase.overloads[0].implementation = function (db) {
            if (file) {
                var send_data = {};
                send_data.type = 'frida-SQLite-delete'
                send_data.data = {
                    'db_path':db.getPath() ? db.toString() : 'null',
                }
                send(send_data);
            }
            return this.deleteDatabase.apply(this,db);
        }
        SQLiteDatabase.deleteDatabase.overloads[1].implementation = function (db,bool) {
            if (file) {
                var send_data = {};
                send_data.type = 'frida-SQLite-delete'
                send_data.data = {
                    'db_path':db.getPath() ? db.toString() : 'null',
                }
                send(send_data);
            }
            return this.deleteDatabase.apply(this, db,bool);
        }
    }
});