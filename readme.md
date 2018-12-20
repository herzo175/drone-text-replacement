# Drone Text Replacement

This is a drone plugin for replacing text in a file from a mapping in a drone
step. You can use this to temporarily substitute tags and secrets at build time

## Usage

Just set the mappings through the plugin settings. The keys must be uppercase
in the target file and be surrounded by handlebars ({{ <word> }}). Only the
filename setting is mandatory

* .drone.yml:

```yaml
kine: pipeline
name: example

steps:
  - name: replace-text
    image: jeremyaherzog/drone-text-replacement
    settings:
      filename: deployment.yaml
      version: ${DRONE_COMMIT_SHA}
```

* deployment.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: yourapp-deployment
spec:
  selector:
    matchLabels:
      app: yourapp
  replicas: 1
  template:
    metadata:
      labels:
        app: yourapp
    spec:
      containers:
      - name: yourapp
        image: yourapp:{{VERSION}}
        ports:
        - containerPort: 80
```