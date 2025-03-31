
param projectName string
// param adminPrincipalId string
param tags object

module appInsightsModule './project-appinsights.bicep' = {
  name: '${deployment().name}-appInsightsDeploy'
  params: {
    projectName: projectName
    tags: tags
  }
}
