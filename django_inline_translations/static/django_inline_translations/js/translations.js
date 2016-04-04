(function(){
    var DjangoTranslator = function() {
        this.editConsole = null;
        this.editConsoleEdit = null;
        this.editConsoleSave = null;

        this.halloSelector = 'span.django-inline-translate';
        this.halloPlugins = {
            'halloformat': {},
            'halloreundo': {},
            'hallolink': {}
        };

        this.url = '/django-inline-translate/';

        this.init = function() {
            this.editConsole = $('<div>').addClass('django-inline-translate-edit-console').appendTo($('body'));
            this.editConsoleEdit = $('<a>').attr('href', '#').addClass('edit').text('Edit').appendTo(this.editConsole);
            this.editConsoleSave = $('<a>').attr('href', '#').addClass('save').text('Save').hide().appendTo(this.editConsole);

            // handlers

            this.editConsoleEdit.click((function(){
                this.editStart();
                return false;
            }).bind(this));

            this.editConsoleSave.click((function(){
                this.editSave();
                return false;
            }).bind(this));
        };

        // Start editing

        this.editStart = function() {
            this.editConsoleEdit.hide();
            this.editConsoleSave.show();

            // init hallo

            $(this.halloSelector).hallo({plugins: this.halloPlugins});
            $(this.halloSelector).addClass('active');
        };

        // Save editing

        this.editSave = function() {
            var modified = {};
            $(this.halloSelector + '.isModified').each(function(){
                modified[$(this).data('translate-id')] = $(this).html();
            });

            $.ajax({
                url: this.url,
                method: 'POST',
                data: modified
            }).done((function(){
                this.saveSuccess();
            }).bind(this)).fail((function(){
                this.saveFailed();
            }).bind(this));
        };

        this.saveSuccess = function() {
            console.log('SAVED');

            this.editConsoleEdit.show();
            this.editConsoleSave.hide();

            // init hallo

            $(this.halloSelector).hallo('destroy');
            $(this.halloSelector).removeClass('active');
        };

        this.saveFailed = function() {
            console.log('FAILED');
        };

        this.init();
    };


    jQuery(window).load(function () {
        new DjangoTranslator();
    });
})();