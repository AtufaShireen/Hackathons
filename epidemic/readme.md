# Epidemic: IIT mandi - Epidemology simulation problem.
Stood 1st position

# PS (stage 1,2,3):
* Reduce death retes with not more than 70% reduction from workplaces.
* Initialise simulation object using covasim model, with the parameters.
* Introduce 3 new variants.
* use interventions to control peak of death tolls by creating effective policies.
* gradually lift all interventions after 2 months.


# Solution:

### stage0
* start day : ‘2021-04-01’
* ~ 800 cumalitive deaths till 2021-09-01.
* ~ 100,000 cumalitive infections till 2021-07-01.(every person can get infected).

### stage 1
* start_day: ‘2021-05-17’, end_day: ‘2021-07-05'.
* cum deaths till end of stage decreased to ~400.
* cum new infections till end of this stage decreased to ~90,000.
* Interventions:
    1. removing mobility by 50% on each day in workplaces from ‘2021-05-17’ till ‘2021-07-01’


### stage 2
* start_day : 2021-07-05, end_day: 2021-09-05.
* cum deaths: ~ 900 by the end of this stage.
* cum new infections: 0 for this stage.
* 3 new variants introduced.
* Interventions:
    1. mandatory use of masks, sanitizers from 2021-07-05 till 2021-09-05 which should reduce the transmition by atleast 5%.
    1. First dose for all, on 10th of july, 20th of july, 30th of july, 9th of august, 19th of august,29th of august with given age priority.This should maake people 80% less prone to get infected and 6% chances of still having symptoms.
    2. Closed schools from 2021-07-05 till 2021-09-05.
    3. work places mobility still locked till 2021-09-05.
    3. testing mandated for people with symptoms(more like to be positive), ~ 500 each day.
    4. 14 days quarantine for positivly diagnoised people.
    5. closing 80 % communities (transports, hotels, day curfew, malls) when the cummulative infections surpasses 500.

### stage 3
* start_day: 2021-09-06.
* end_day: 2021-11-06.

* interventions:
    1. Second drive of vaccine (for first and second dose): on 28th of sep, 8th of oct, 18th of oct.
    2. mask, sanitizers still mandatory till 20th of oct.
    3. school lockdown lifted from 20th of oct.
    4. workplaces lockdown reduced to 10% from 6th of september till 18th of oct then lifted completely..
    4. schools lockdown reduced to 10% from 6th of september till 18th of oct then lifted completely..
    6. dynamic community lockdown lifted completely from 7th of november.
    7. mandatory testing removed from 2021-11-06.

