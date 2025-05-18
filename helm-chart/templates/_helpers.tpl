{{- define "fastapi-stateful.name" -}}fastapi-stateful{{- end }}
{{- define "fastapi-stateful.fullname" -}}{{ .Release.Name }}-{{ include "fastapi-stateful.name" . }}{{- end }}
{{- define "nginx.fullname" -}}{{ .Release.Name }}-nginx-proxy{{- end }}
{{- define "redis.fullname" -}}{{ .Release.Name }}-redis{{- end }}