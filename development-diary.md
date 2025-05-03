# Development diary

Full video recordings for the following logs from
my
[X](
  https://x.com/truocolo).
profile are linked in the headers for the
following logs.

Of course I do kinda try to entertain the
viewers of these recordings somehow
when I'm in the mood, so their lengths
do not represent the actual time
spent on solving the problem;
still they do include the actual
reasoning behind the changes in the
code.

Also further than this log you have
available for eventual quicker checking
this repository's git logs and the
concrete commits.

## April 28th 2025

### 00:00

For now I've added a stub `shop` Python module.

### 01:00

It seems appropriate to me to just write a simple
application to use as a wrapper specifically
for the request.

I'm probably gonna call the application
`mysterious-shop`.

### 01:30

Having to fill and send the request's completion in
a form on a transient web page without knowing
the exact deadline and if and when the address
could become invalid kinda gives me some anxiety
given my current work schedule,
so since no specific request seems to have been made
to keep any of the information regarding this
assessment private I think I will just make this
repository public while redacting the identity of
the involved parties and immediately send the request. 

## April 29th 2025 

### [5:00-6:30](https://x.com/truocolo/status/1916720123366277193)
Since I'm travelling and I'm from the Android environment
and I've discovered there's no IPython development environment
packaged for Android, I've spent this hour and half start packaging
it for Life and DogeOS.
I've also deemed appropriate to livestream the work on this
repository and of the others on X.

I've packaged the program I'm writing under
[mysterious-shop](
  https://github.com/themartiancompany/mysterious-shop-ur)
and
[mysterious-shop-git](
  https://github.com/themartiancompany/mysterious-shop-git-ur).

### [17:00-18:00](https://x.com/truocolo/status/1916868716026908970)

On this session I just package a couple dependencies for
IPython.

### 19:00

I need to sleep.

The development livestreams recording for this
assessment are published on x.com/truocolo, just
in case.

## April 30th 2025

### [21:00-01:00](https://x.com/truocolo/status/1917708259844124793)

I do package more IPython dependencies for Life and
DogeOS Android bases.

## 1th May 2025

### [12:00-13:00](https://x.com/truocolo/status/1917902574742651129)

IPython for Life and DogeOS Android bases has been
packaged and made uncensorable on the
[Ur](
  https://github.com/themartiancompany/ur)
application store.
An HTTP mirror is available at
[ipython-ur](
  https://github.com/themartiancompany/ipython-ur).

Now that I have the development tool needed to
comfortably complete the assessment, I can
concretely start working on it.

### [13:30-16:30](https://x.com/truocolo/status/1917967688220987444)

Complete implementation for an `AppConfig`
application configuration class.
Complete implementation for a `DbManager` databases'
manager class.
Start implementing a `ZoneManager` zones' manager
class.

### [18:00-21:30](https://x.com/truocolo/status/1918040194487382256)

Finish implementing `ZoneManager` and
`ItemManager` as in how I initially got the
E-commerce website worked.

At the moment of writing the requested optimization function
though and the CartManager class, so reading the
*total discount percentage* can actually
be higher than the *per-item discount percentage* I do realize
there's actually two discount rates involved in this optimization
problem, one depending on the zone and another depending on the
item, thus requiring some small changes to the data structures
already implemented.

## 2th May 2025

### [17:00-20:30](https://x.com/truocolo/status/1918374720413524406)

Adjust the existing classes for the two discount rates;
add `categories_manager.py` and its `CategoriesManager` class,
start writing the init functions and store settings.

## 3th May 2025

### 01:00-3:20

Finishing implementing store settings together with
a set of defaults, documented most classes and methods,
properly renamed some functions to set up
a stable reading/writing pattern for user-developers who could have
to deal with this code in the future.

So more or less I've like written almost a whole store application
implementing the constraints to write the solver the request asks for.

While one may observe doing this could have been kinda of an overshot,
to a careful examiner who was to look at
[my previously published projects](
  https://github.com/themartiancompany/ur)
it could be apparent I may already needed some of
this code I've written for
[purposes](
  https://x.com/truocolo/status/1918387814145630213)
related to those projects.
