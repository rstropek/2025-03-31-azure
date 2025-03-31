param projectName string
//param adminPrincipalId string
param tags object

var infraTags = union(tags, {
  Type: 'central-infrastructure'
})

module acrModule './central-acr.bicep' = {
  name: '${deployment().name}-acrDeploy'
  params: {
    projectName: projectName
    //adminPrincipalId: adminPrincipalId
    tags: infraTags
  }
}
