# datathon


## Data Metrics (Data Analysis)

To create an accurate measurement of the business of each port at the borders, we decided to normalize the data points and compute an aggregated score.
Step 1: We normalized each measure on a scale of 0-1 by dividing by the maximum value of that value across all ports. 

          Normalized Measure = Max Measure Value/Measure Value

          # Normalize measures
          for measure in measure_traffic_pivot.columns[1:]:
              measure_traffic_pivot[measure] = measure_traffic_pivot[measure] / measure_traffic_pivot[measure].max()

Step 2: We decided to assign a weight to each normalized measure. We assigned the weights based on time taken to cross the border.

          weights = {
              'Bus Passengers': 0.1,
              'Buses': 1,
              'Pedestrians': 0.1,
              'Trains': 0.5,
              'Trucks': 0.5,
              'Personal Vehicle': 0.3
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

          # Rank ports based on the composite metric
          port_metrics['Rank'] = port_metrics['Composite Metric'].rank(ascending=False)
          port_metrics = port_metrics.sort_values('Rank')
 

