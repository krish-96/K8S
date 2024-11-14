#!/bin/bash
#for i in $(seq 1 20); do
##  output="$(curl -s --resolve echo.prod.mydomain.com:80:$INGRESS_CONTROLLER_IP echo.prod.mydomain.com )" | grep "Hostname";
#  minikubeIp=$(minikube ip)
#  output=$(curl -s --resolve echo.prod.mydomain.com:80:$minikubeIp echo.prod.mydomain.com | grep "Hostname")
#  echo $output
#  done

echo "FileName $0 "
echo "No of Requests: "


# Initialize counters

if echo $1; then
  number_of_requests=$1
else
  number_of_requests=100
fi

production_count=0
canary_count=0

# Run a larger number of requests to improve accuracy
for i in $(seq 1 $number_of_requests); do
  minikubeIp=$(minikube ip)
  output=$(curl -s --resolve echo.prod.mydomain.com:80:$minikubeIp echo.prod.mydomain.com | grep "Hostname")

  # Increment appropriate counter based on the hostname output
  if echo "$output" | grep -q "production"; then
    production_count=$((production_count + 1))
  elif echo "$output" | grep -q "canary"; then
    canary_count=$((canary_count + 1))
  fi

  # Print each output for reference (optional)
  echo "$output"
done

# Display final counts and percentage
total_requests=$((production_count + canary_count))
canary_percentage=$(echo "scale=2; ($canary_count / $total_requests) * 100" | bc)
production_percentage=$(echo "scale=2; ($production_count / $total_requests) * 100" | bc)

echo ""
echo "Summary:"
echo "Total requests: $total_requests"
echo "Production count: $production_count (${production_percentage}%)"
echo "Canary count: $canary_count (${canary_percentage}%)"
