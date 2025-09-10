# Problem Statement:

Design a dashboard to visualize trip details across the city, focusing on trips with durations of x minutes. The dashboard should display the start and end points of each trip on a map and use color-coding to differentiate trips based on their duration.
With the following requirements:

Display the start and end points of each trip on a map.
Connect the start and end points with colored lines to represent the trips.
Apply the following color-coding scheme to the lines and points based on trip duration:
Color 'A' for trips lasting less than 5 minutes.
Color 'B' for trips lasting between 6 to 15 minutes.
Color 'C' for trips lasting between 16 to 20 minutes.
Color 'D' for trips lasting between 21 to 30 minutes.
Color 'E' for trips lasting more than 30 minutes.


## Expected Technical Constraints:
Volume Handling: The trip data received every minute can be more than a GB,( as zypp plans to reach the goal of adding ~200000 vehicles in the fleet and has been in operation since 2017) and hence complete data cannot be consumed at once. 
Frontend Capacity: Frontend of the dashboard cannot consume more than 5000 points at once. 
Display Limit: The dashboard should limit the display to a maximum of 500 points (say g) on the overview to ensure clarity and readability.

## Meeting the technical constraints:
Volume Handling: Using batching we can divide the data into fixed size, and easily add and then remove from the backend of the dashboard.
Frontend Capacity: reduce/combine points at the backend rather than after receiving on the frontend.
Display Limit: Use a clustering approach to combine similar points.

## Limitations:
The points on the dashboard are aggregated and hence does not represent the actual data but a similar distribution of the data.
The trip durations are averaged, and the standard deviation is ignored, and hence the underlying trip duration of a line coded as D can deviate by +- x mins.

Note: A numerical accuracy of the above limitations should be calculated and reported. 

## Estimated Time Required:
While this also depends on the techstack and current data base schema, I believe most of the time will be taken by deciding the parameters of the clustering algorithm and batch size which needs an understanding of the underlying data distributions.

## Success Metric:
With the HEART Goal:
Happiness: Displaying the dashboard in a readable format. (Feedback)
Engagement: Usefulness of the dashboard. (number of features added / number of intended features)
Adoption: Adding the new points. (memory available)
Retention: caching the previous points. 
Task: Loading the dashboard with low latency. (time taken to render dashboard)

## Closing Notes:
The dynamic loading and regeneration of the dashboard is not considered.
An alternative approach to using clustering method, is to calculate the an h3 hash of every lat,long point with a fixed resolution of 8. (say, ~0.7km2) to combine similar start and end point.
