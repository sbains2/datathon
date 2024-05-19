# datathon
# Government: Analyzing and Predicting Inbound Crossings the U.S.-Canada and the U.S.-Mexico border

The goal of our project this weekend was to analyze the effect of COVID-19 on inbound traffic crossings between the U.S.-Canada and the U.S.-Mexico border. We wanted to analyze the efficiency and volume of traffic at each entry port, looking for various factors affecting long wait times. Additionally, we wanted to provide a solution for our peers and fellow travelers to efficiently plan vacations across the border without dealing with unforeseen wait times. 

Initially to understand the data we conducted a descriptive analysis of our dataset after splitting it into two categories: Mexican borders and Canadian borders. This helped us narrow down each port and understand their traffic movements for their respective regions. Another factor we decided to include in our analysis is seasonal weather. We classified each month as a fall, spring, summer, or winter month. This showed us that during the summer and fall seasons, the Canadian border has the most inbound traffic while the Mexico border has constant high-volume traffic throughout every season. 
_**Link to boxplot graph:**_ https://public.tableau.com/app/profile/anirit.bansal/viz/BorderTraffic/Sheet3

<p align="center">
   <img width="300" alt="Screenshot 2024-05-19 at 11 14 39 AM" src="https://github.com/sbains2/datathon/assets/67097552/e457614a-1e14-4a75-8e99-9b0a0eee1484">
  <img width="300" alt="Screenshot 2024-05-19 at 11 20 15 AM" src="https://github.com/sbains2/datathon/assets/67097552/e4fdc872-d9b1-409f-823b-a40ae569057c">
   <img width="300" alt="Screenshot 2024-05-19 at 11 08 01 AM" src="https://github.com/sbains2/datathon/assets/67097552/81f926db-76aa-4b0b-aed2-3a24b0028ac4">
</p>

**Mexican Border:** 
- 2017-2019: The median inbound traffic is around 1,917,000 with a spread ranging from approximately 1,442,000 to 2,470,000. There are outliers on both the higher and lower ends, suggesting occasional spikes and dips in traffic volume.
- 2020-2021: The median inbound traffic is around 1,621,000 with a spread ranging from approximately 1,315,000 to 1,917,000. The spread and the median have both decreased compared to the previous period, suggesting a more inconsistent flow of traffic. There are outliers on both ends, but less frequent than in the first period.
- 2022-2024: The median inbound traffic is around 1,827,000 with a spread ranging from approximately 1,500,000 to 2,144,000. The spread and median show some recovery compared to the Covid period but haven't reached the levels seen in 2017-2019. There are outliers on both ends, similar to the first period. Even if the same levels were reached, our data did not reflect such.

  
**Canadian Border:**
- 2017-2019: The median inbound traffic is around 1,389,000 with a spread ranging from approximately 1,019,000 to 1,979,000. The spread is smaller than the Canadian Border, indicating a tighter distribution of traffic volume. There are also fewer outliers compared to the Canadian Border.
- 2020-2021: The median inbound traffic is around 1,387,000 with a spread ranging from approximately 1,064,000 to 1,709,000. Similar to the Mexican Border, the spread and median decreased, indicating a more inconsistent traffic flow. There are outliers on both ends, but less frequent than in the first period.
- 2022-2024: The median inbound traffic is around 1,562,000 with a spread ranging from approximately 1,209,000 to 1,970,000. Similar to the Mexican Border, the spread and median show some recovery but haven't reached pre-Covid levels. There are outliers on both ends, but less frequent than in the first period. Even if the same levels were reached, our data did not reflect such.

In summary, analyzing inbound traffic between the Canadian and Mexican Borders across three periods (2017-2019, 2020-2021, 2022-2024) reveals a pattern potentially linked to the Covid-19 pandemic. The spread of traffic volume, indicating seasonal variations, was significantly wider for the Mexican Border across all periods (Mexican Border spread: 1,028,000 vs. Canadian Border spread: 960,000 in 2017-2019). Notably, both borders experienced a tightening of this spread during the Covid period (2020-2021), with medians around 1,621,000 (Mexico) and 1,387,000 (Canada), suggesting a more consistent flow of traffic likely due to travel restrictions. While the most recent period (2022-2024) shows some recovery in spread and medians, they haven't reached pre-pandemic levels, indicating lingering effects or a new normal for border traffic.


After noticing such a discrepancy, we still were curious about the highly consistent trends of inbound traffic so we decided to further break down our two data of inbound traffic crossings between the U.S.-Canada and the U.S.-Mexico border into 3 new categories:
1. Distribution of inbound traffic for each port per year

   
           <Viz Canada 1.2.1> <Viz Mexico 1.2.2> 
3. Distribution of traffic per year at the Mexican border
          <Viz Canada 1.3.1> <Viz Mexico 1.3.2> 
4. Distribution of inbound traffic per state
          <Viz Canada 1.4.1> <Viz Mexico 1.4.2> 


   
## Data Metrics (Data Analysis)

To create an accurate measurement of the traffic at each port at the borders, we decided to norma<img width="1106" alt="Screenshot 2024-05-19 at 10 15 36 AM" src="https://github.com/sbains2/datathon/assets/67097552/e4d3ddd2-2df2-4204-b7e4-33cffbeab4f9">
lize the data points and compute an aggregated score, ranking each port based on the busiest port. To do so we created the following metric that encompassed the majority of the factors affecting border wait times.

Step 1: We normalized each measure on a scale of 0-1 by dividing by the maximum value of that value across all ports. 

          Normalized Measure = Max Measure Value/Measure Value

          # Normalize measures
          for the measure in measure_traffic_pivot.columns[1:]:
              measure_traffic_pivot[measure] = measure_traffic_pivot[measure] / measure_traffic_pivot[measure].max()

Step 2: We decided to assign a weight to each normalized measure. We assigned the weights based on the time taken to cross the border.

          weights = {
              'Bus Passengers': 0.1,	
              'Buses': 2,	
              'Pedestrians': 0.1,
              'Personal Vehicle Passengers': 0.1,
              'Personal Vehicles': 1,	
              'Rail Containers Empty': 0.2,
              'Rail Containers Loaded': 1,
              'Train Passengers': 0.1,
              'Trains': 2,
              'Truck Containers Empty': 0.2,
              'Truck Containers Loaded': 1,
              'Trucks': 2
          }
​
Step 3: After assigning weights to each variable and normalizing measures, we calculated the composite score by summing the weighted normalized measures.

          $$
          \sum_{i=1}^{n} w_{i} \times \text{Normalized Measure}_{i}
          $$
          
          measure_traffic_pivot['Composite Metric'] = sum(
              weights[measure] * measure_traffic_pivot[measure] for measure in weights
          )
​
Step 4: Now that the composite metric has been created, all we had to do was rank the ports

          port_metrics['Rank'] = port_metrics['Composite Metric'].rank(ascending=False)
          port_metrics = port_metrics.sort_values('Rank')


### Outcome:
This metric not only helped us understand the busiest ports during a certain time of the year but also helped us create a machine-learning model recommendation system, providing individuals entering the US with optimized information regarding which is the best port to use based on the date of travel. Our algorithm created above to compute the composite metric showed to have an 85% feature importance on predicting recommended ports for users.

<img width="886" alt="Screenshot 2024-05-19 at 9 36 11 AM" src="https://github.com/sbains2/datathon/assets/67097552/c79f0cea-5189-4d49-adc6-a1ef7bbafde2">

With the new composite metric having such an effect on the prediction values, we decided to rank each port from most busiest to least, using composite metric. We were able to implement this ranking system on our map visualization showing the top 20 locations that are the busiest that are recommended to avoid. While this may not seem like much, from this composite score we can infer:
- Ports with higher ranks might need to allocate more resources, infrastructure, and staffing to handle high traffic.
- By identifying the busiest ports, officials can optimize operations at these locations.
- Ports with the busiest wait time can strategically plan for future investments and expansion projects.
- The ranks highlight whether traffic is concentrated in a few major ports or more evenly distributed across several ports, helping guide policies to balance traffic loads and avoid bottlenecks.
- Critical ports that need robust emergency and contingency planning.

  Link to map: https://public.tableau.com/app/profile/sahil.bains/viz/MeasuringDensityAmongTop20RankedBusiestBorderCrossings/Sheet2
  


