class WISRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'wis':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'wis':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._state.db == 'default' or obj2._state.db == 'default':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'wis':
            return db == 'default'
        return None

class WADRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'wad':
            return 'wad'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'wad':
            return 'wad'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._state.db == 'wad' or obj2._state.db == 'wad':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'wad':
            return db == 'wad'
        return None
