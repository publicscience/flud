# FLUD

Visual Twitter streams for queries.

## Setup

* Setup `config.py`
    * Setup your Twitter info (Visit
        [https://apps.twitter.com/](https://apps.twitter.com/) to set it
        up if you need to.)
    * Set a login username and password
* Setup a virtualenv
    * `virtualenv ~/env/flud --no-site-packages`
    * Activate it: `source ~/env/flud/bin/activate`
* Install dependencies: `pip install -r requirements.txt`
* Run the server: `python application.py`
* Follow a twitter query/story visually: `localhost:5000/_ferguson`. Use
`_` to represent a hash (`#`) since hashes in urls aren't passed to the
backend.

If you're deploying it to a server, you can use the setup script in
`setup/setup.sh`.

*Note*: if you have Disconnect or a similar social-blocking plugin,
you may need to disable it to get the images to load properly.
