# Analysis of voting blocs in United Nations

The following project сontains a proposal of a model to distinguish voting blocs in various councils, using a case of UN General Assembly as the main case.

# Structure

The structure of the project as implemented are following 3 modules:

scrubber -- implements a simple scrubbing algorithm to extract voting records in UN's General Assembly over a given time period. The implementation is matter-of-need and as such has some considerable flaws such as

- Is not very compatible with multiple renaming UN members went through during it's long history. There is a hardcoded implementation to consider renamings over periods of 1965-1980 years and 2007-present day, so those 2 periods are known to work properly.

- Does not remove countries that were too young to participate in votes properly.

model -- the actual proposed model, based around optimizing a smoothed piecewise-linear functional over discrete distributions (one per vertex). Functionally this model groups together countries that cannot be part of the same voting bloc. See related details in docs/model.org

votinggraph -- the module that ties above together to provide straightforward means of producing processed in the sense of model above vote graphs. Also contains the function that nice-prints the 2 communities for reporting purposes.

# Additional information

See docs/results.org on overall results of the research

# Creators

Shuklov Yuri

Stetskevich Artemii
