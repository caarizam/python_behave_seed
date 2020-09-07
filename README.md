# Automation Framework Seed with Python and Behave

## How to execute all files:
behave 

## How to execute a single file:
behave SampleE2E.feature

## How to execute a tag:
behave SampleE2E.feature --tags=regression

## How to execute the tag @smoke or the tag @regression:
behave SampleE2E.feature --tags=smoke,regression

## How to execute the tag @smoke and the tag @regression:
behave SampleE2E.feature --tags=smoke --tags=regression

## How to exclude the tag '~' @smoke:
behave SampleE2E.feature --tags=-smoke --tags=regression