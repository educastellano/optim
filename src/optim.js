
(function (root) {
    'use strict';

    // Define some helper functions
    //
    var loadScript,
        loadSync,
        loadAllScripts;

    loadScript = function (url, callback) {
        var head,
            script;

        script = document.createElement('script');
        script.type = 'text/javascript';
        script.src = url;

        if (callback) {
            script.onreadystatechange = callback;
            script.onload = callback;
        }

        head = document.getElementsByTagName('head')[0];
        head.appendChild(script);
    };

    loadSync = function (filePath, mimeType) {
        var xmlhttp,
            resp;

        xmlhttp = new XMLHttpRequest();
        xmlhttp.open("GET", filePath, false);
        if (mimeType) {
            if (xmlhttp.overrideMimeType) {
                xmlhttp.overrideMimeType(mimeType);
            }
        }
        xmlhttp.send();
        if (xmlhttp.status === 200) {
            resp = xmlhttp.responseText;
        }

        return resp;
    };

    loadAllScripts = function (files, i) {
        if (files[i]) {
            loadScript(files[i], function () {
                loadAllScripts(files, ++i);
            });
        }
    };
    
    // Load the script(s)
    //
    var json_config,
        config;

    json_config = loadSync(root.__optim_file__);
    if (json_config) {
        config = JSON.parse(json_config);
        if (window.location.hostname.indexOf('localhost') === -1) {
            loadScript(config.minified_file + '?v=' + config.version);
        }
        else {
            loadAllScripts(config.files, 0);
        }
    }

})(this);