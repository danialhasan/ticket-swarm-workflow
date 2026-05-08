# Shifted Schedule Math

Use this reference when work started later than the original baseline.

## Core rule

Shift the entire baseline and every gate date by the same number of business days.

Do not:

- rewrite only today's target
- keep old gate dates while shifting ticket targets
- describe the correction only with relative dates

## Outputs to compute

- shifted previous business-day close target
- shifted current-day close target
- shifted next gate date and name
- exact ahead/on/behind delta

## Reporting rules

- always use absolute dates
- report the shifted schedule explicitly
- if the target changed because of a slip, state the slip and the business-day shift count

## Example posture

If the baseline started one business day late:

- every baseline date moves one business day later
- every gate date moves one business day later
- behind-amount = shifted current-day target minus current Done count
