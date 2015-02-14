### Movie trailer site

A basic site for browsing movie posters and viewing trailers.

### Usage

The repo should contain a few python source files:

``` bash
    [rule146@rule146: movie-trailer-site]$ ls -1
    entertainment_center.py
    fresh_tomatoes.py
    media.py
```

Run the code for dynamically generating the html source:

``` bash
    [rule146@rule146: movie-trailer-site]$ python entertainment_center.py
```

A browser tab should open, showing the generated site:

![movie trailer
site](/images/site.png)

Hover over a movie poster to see a synopsis:

![movie
synopsis](/images/synopsis.png)

Click a movie poster to view the trailer in a popup:

![movie
trailer](/images/trailer.png)

### Attribution

This is almost entirely boilerplate code provided by Udacity as a warm-up
exercise for the [full-stack web dev nanodegree](https://www.udacity.com/nanodegree).

I provided the movie synopses, and most of the movie choices.
