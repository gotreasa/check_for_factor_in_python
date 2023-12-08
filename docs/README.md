# Check_for_Factor_in_Python

[![License: AGPL](https://img.shields.io/badge/License-AGPL-blue.svg)](https://github.com/gotreasa/check_for_factor_in_python/blob/main/LICENSE)
[![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=gotreasa_check_for_factor_in_python&metric=alert_status)](https://sonarcloud.io/dashboard?id=gotreasa_check_for_factor_in_python)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=gotreasa_check_for_factor_in_python&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=gotreasa_check_for_factor_in_python)
[![Build Status](https://github.com/gotreasa/check_for_factor_in_python/actions/workflows/cicd.yml/badge.svg)](https://github.com/gotreasa/check_for_factor_in_python/actions/workflows/cicd.yml)
[![Can I Deploy main to test](https://gotreasa.pactflow.io/pacticipants/check_for_factor_in_python_app/branches/main/latest-version/can-i-deploy/to-environment/test/badge)](https://gotreasa.pactflow.io/hal-browser/browser.html#https://gotreasa.pactflow.io/pacticipants/check_for_factor_in_python_app/branches/main/latest-version/can-i-deploy/to-environment/test/badge)

Welcome to the Python Template created via a cookiecutter recipe. The project template is designed for a development via a `Double Loop approach` (BDD-TDD) using pytest and several other pytest libs.

## Description

This function should test if the factor is a factor of base.

Return `true` if it is a factor or false if it is not.

### About factors

Factors are numbers you can multiply together to get another number.

2 and 3 are factors of 6 because: `2 * 3 = 6`

You can find a factor by dividing numbers. If the remainder is 0 then the number is a factor.
You can use the mod operator (`%`) in most languages to check for a remainder
For example 2 is not a factor of 7 because: `7 % 2 = 1`

Note: `base` is a non-negative number, `factor` is a positive number.
