param (
  [parameter(mandatory=$true)]$title,
  [string]$description,
  [parameter(mandatory=$true)][string]$labels,
  [parameter(mandatory=$true)][int]$priority,
  [parameter(mandatory=$true)][string]$due_string,
  [parameter(mandatory=$true)][int]$project_id,
  [parameter(mandatory=$true)][string]$token
)

$body = @{
  "content" = $title
  "description" = $description
  "labels" = $labels -split ', |,'
  "priority" = $priority
  "due_string" = $due_string
  "project_id" = $project_id
} | ConvertTo-Json

$headers = @{
  'Content-Type' = 'application/json'
  'Authorization' = "Bearer ${token}"
}

$output = (
  Invoke-RestMethod -uri https://api.todoist.com/rest/v2/tasks `
    -method 'Post' `
    -headers $headers `
    -body $body
)

$output

# if ($output -eq 200) {
# Get-Content response.txt
# } else {
#     Write-Error "Unexpected response $output"
#     Get-Content response.txt
# }

break

# # escapes double quotes (because why? curl rejects it otherwise, something to explore later)
# $data = $data -replace '"', '\"'
# 
# # creates task, stores response in response.txt, collects response code in $output
# $output = (curl -X POST https://api.todoist.com/rest/v2/tasks --data $data -H "Content-Type: application/json" -H "Authorization: Bearer ${{ secrets.token"  -s -o response.txt -w "%{http_code}")
# 
# # checks output, returns response but fails if not 200
# if ($output -eq 200) {
# Get-Content response.txt
# } else {
#     Write-Error "Unexpected response $output"
#     Get-Content response.txt
# }