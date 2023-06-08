# JupyterLite Demo

[![lite-badge](https://jupyterlite.rtfd.io/en/latest/_static/badge.svg)](https://jupyterlite.github.io/demo)

JupyterLite deployed as a static site to GitHub Pages, for demo purposes.

## ✨ Try it in your browser ✨

➡️ **https://jupyterlite.github.io/demo**

![github-pages](https://user-images.githubusercontent.com/591645/120649478-18258400-c47d-11eb-80e5-185e52ff2702.gif)

## Requirements

JupyterLite is being tested against modern web browsers:

- Firefox 90+
- Chromium 89+

## Deploy your JupyterLite website on GitHub Pages

Check out the guide on the JupyterLite documentation: https://jupyterlite.readthedocs.io/en/latest/quickstart/deploy.html

## Further Information and Updates

For more info, keep an eye on the JupyterLite documentation:

- How-to Guides: https://jupyterlite.readthedocs.io/en/latest/howto/index.html
- Reference: https://jupyterlite.readthedocs.io/en/latest/reference/index.html

## Developer Guide

First, set up the enviornment:
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

pip install -e path/to/monorepo/mitosheet
pip install jupyter_packaging
jupyter labextension develop path/to/monorepo/mitosheet --overwrite
```

Then, build JupyterLite:
```
jupyter lite build
```


Then, in `monorepo/mitosheet` start your virtual environment, and start `jswatch` as normal. You might start this by running `jlpm run watch`.

Finally, install the mito Python package for development. 

In `monorepo/mitosheet` folder, create a wheel, and lint it into JupyterLite:
```
python3 setup.py bdist_wheel
ln -s /absolute/path/to/monorepo/mitosheet/dist/mitosheet-0.3.131-py2.py3-none-any.whl /absolute/path/tomitolite/_output/extensions/@jupyterlite/pyodide-kernel-extension/static/mitosheet-0.3.131-py2.py3-none-any.whl
```

Then, in the mitolite folder, launch a server:
```
python test_server.py
```

Then, open Google Chrome, go to private browsing and paste in `localhost:8000`. 

Create a new notebook and run:
```
import piplite
await piplite.install('mitosheet-0.3.131-py2.py3-none-any.whl', deps=False)
%pip install pandas plotly openpyxl distutils chardet requests analytics-python pyodide-http
```

Then, you can use mitosheet. **Everything should be working as normal, albeit a bit slower as nothing is threaded!**

## Making changes to mitosheet and seeing the new version

### Changing the Python code or to the Mito widget

If you make changes to the Python code of mitosheet, and you want to use this new code, simply run:
```
python3 setup.py bdist_wheel
rm /absolute/path/tomitolite/_output/extensions/@jupyterlite/pyodide-kernel-extension/static/mitosheet-0.3.131-py2.py3-none-any.whl
ln -s /absolute/path/to/monorepo/mitosheet/dist/mitosheet-0.3.131-py2.py3-none-any.whl /absolute/path/tomitolite/_output/extensions/@jupyterlite/pyodide-kernel-extension/static/mitosheet-0.3.131-py2.py3-none-any.whl
```
If you make changes to the JS code under the Mito widget (e.g. not touching the JLab integration), then the above commands will also work.

### Changing the extension code

If you update `extension.tsx` or other files touching the JLab integration, you need to rebuild the JupyterLite application by:
1. Shutting down the test server.
2. `jupyter lite build`
3. `python test_server.py`

# Some Notes
1. Use Chrome Private Browsing. You can't access files in Firefox private browsing (see here: https://jupyterlite.readthedocs.io/en/latest/howto/configure/advanced/service-worker.html#limitations)

## On Piodide limitations:
See here: https://pyodide.org/en/stable/project/roadmap.html#write-http-client-in-terms-of-web-apis

Python packages make an extensive use of packages such as requests to synchronously fetch data. We currently can’t use such packages since sockets are not available in Pyodide. We could however try to re-implement some stdlib libraries with Web APIs, potentially making this possible.

Because http.client is a synchronous API, we first need support for synchronous IO.
