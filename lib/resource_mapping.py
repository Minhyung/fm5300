
# Automatically generated at: 2018-07-03 11:42:10
# Number of APIs fetched: 81
# GigaVUE-FM 5.3 Core APIs

RESOURCE_MAPPING_v13 = {
    "appFilterRsc": {
        "methods": [
            "GET"
        ],
        "resource": "/appFilterRsc"
    },
    "appFilterRscslotId": {
        "methods": [
            "GET"
        ],
        "resource": "/appFilterRsc/{slotId}"
    },
    "appsgtpwhitelists": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/apps/gtp/whitelists"
    },
    "appsgtpwhitelistsalias": {
        "methods": [
            "DELETE"
        ],
        "resource": "/apps/gtp/whitelists/{alias}"
    },
    "appsgtpwhitelistsaliasentries": {
        "methods": [
            "GET",
            "POST",
            "DELETE"
        ],
        "resource": "/apps/gtp/whitelists/{alias}/entries"
    },
    "appsgtpwhitelistsaliasentriesall": {
        "methods": [
            "DELETE"
        ],
        "resource": "/apps/gtp/whitelists/{alias}/entries/all"
    },
    "appsgtpwhitelistsaliasentriesfile": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/gtp/whitelists/{alias}/entries/file"
    },
    "appsgtpwhitelistsaliasentriesurl": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/gtp/whitelists/{alias}/entries/url"
    },
    "appshsm": {
        "methods": [
            "GET",
            "POST",
            "DELETE"
        ],
        "resource": "/apps/hsm"
    },
    "appshsmGroup": {
        "methods": [
            "POST",
            "DELETE"
        ],
        "resource": "/apps/hsmGroup"
    },
    "appshsmGroupStatusReport": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/hsmGroupStatusReport"
    },
    "appshsmGroupalias": {
        "methods": [
            "GET",
            "PATCH",
            "PUT",
            "DELETE"
        ],
        "resource": "/apps/hsmGroup/{alias}"
    },
    "appshsmGroupaliashsmhsmAlias": {
        "methods": [
            "POST",
            "DELETE"
        ],
        "resource": "/apps/hsmGroup/{alias}/hsm/{hsmAlias}"
    },
    "appshsmGroupaliaskeyHandler": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/hsmGroup/{alias}/keyHandler"
    },
    "appshsmGroupaliaskeyHandlerfile": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/hsmGroup/{alias}/keyHandler/file"
    },
    "appshsmalias": {
        "methods": [
            "GET",
            "PUT",
            "DELETE"
        ],
        "resource": "/apps/hsm/{alias}"
    },
    "appsinlineSsl": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/inlineSsl"
    },
    "appsinlineSslcachingcertValidation": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/inlineSsl/caching/certValidation"
    },
    "appsinlineSslcachingcertValidationfingerprint": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/inlineSsl/caching/certValidation/{fingerprint}"
    },
    "appsinlineSslcachingurl": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/inlineSsl/caching/url"
    },
    "appsinlineSslcachingurldomainPattern": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/inlineSsl/caching/url/{domainPattern}"
    },
    "appsinlineSslprofiles": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/inlineSsl/profiles"
    },
    "appsinlineSslprofilesalias": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/inlineSsl/profiles/{alias}"
    },
    "appsinlineSslprofilesaliasdecrypttcpportMapports": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/inlineSsl/profiles/{alias}/decrypt/tcp/portMap/ports"
    },
    "appsinlineSslprofilesaliasdecrypttcpportMapportsruleId": {
        "methods": [
            "DELETE"
        ],
        "resource": "/apps/inlineSsl/profiles/{alias}/decrypt/tcp/portMap/ports/{ruleId}"
    },
    "appsinlineSslprofilesaliasdecrypttcpportMaps": {
        "methods": [
            "PUT"
        ],
        "resource": "/apps/inlineSsl/profiles/{alias}/decrypt/tcp/portMaps"
    },
    "appsinlineSslprofilesaliaskeyMap": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/inlineSsl/profiles/{alias}/keyMap"
    },
    "appsinlineSslprofilesaliaskeyMapruleId": {
        "methods": [
            "DELETE"
        ],
        "resource": "/apps/inlineSsl/profiles/{alias}/keyMap/{ruleId}"
    },
    "appsinlineSslprofilesaliaskeyMaps": {
        "methods": [
            "PUT"
        ],
        "resource": "/apps/inlineSsl/profiles/{alias}/keyMaps"
    },
    "appsinlineSslprofilesaliaslist": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/inlineSsl/profiles/{alias}/list"
    },
    "appsinlineSslprofilesaliaslistlistType": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/inlineSsl/profiles/{alias}/list/{listType}"
    },
    "appsinlineSslprofilesaliaslistlistTypefile": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/inlineSsl/profiles/{alias}/list/{listType}/file"
    },
    "appsinlineSslprofilesaliaslistlistTypefiledomain": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/inlineSsl/profiles/{alias}/list/{listType}/file/{domain}"
    },
    "appsinlineSslprofilesaliasrule": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/inlineSsl/profiles/{alias}/rule"
    },
    "appsinlineSslprofilesaliasruleruleId": {
        "methods": [
            "DELETE"
        ],
        "resource": "/apps/inlineSsl/profiles/{alias}/rule/{ruleId}"
    },
    "appsinlineSslprofilesaliasrules": {
        "methods": [
            "PUT"
        ],
        "resource": "/apps/inlineSsl/profiles/{alias}/rules"
    },
    "appsinlineSslsigning": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/inlineSsl/signing"
    },
    "appsinlineSsltrustStore": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/inlineSsl/trustStore"
    },
    "appsinlineSsltrustStorecert": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/inlineSsl/trustStore/cert"
    },
    "appsinlineSsltrustStorecertfile": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/inlineSsl/trustStore/cert/file"
    },
    "appsinlineSsltrustStorecertfilefingerprint": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/inlineSsl/trustStore/cert/file/{fingerprint}"
    },
    "appsinlineSsltrustStoredefault": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/inlineSsl/trustStore/default"
    },
    "appsinlineSsltrustStorefile": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/inlineSsl/trustStore/file"
    },
    "appskeystorekeychain": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/keystore/keychain"
    },
    "appskeystorekeychainlock": {
        "methods": [
            "PUT"
        ],
        "resource": "/apps/keystore/keychain/lock"
    },
    "appskeystorekeychainpassword": {
        "methods": [
            "POST",
            "PUT"
        ],
        "resource": "/apps/keystore/keychain/password"
    },
    "appskeystorekeys": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/keystore/keys"
    },
    "appskeystorekeysalias": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/keystore/keys/{alias}"
    },
    "appskeystorekeysaliascertificate": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/keystore/keys/{alias}/certificate"
    },
    "appskeystorekeysfile": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/keystore/keys/file"
    },
    "appskeystorekeysgenerate": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/keystore/keys/generate"
    },
    "appsnetflowexporters": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/apps/netflow/exporters"
    },
    "appsnetflowexportersalias": {
        "methods": [
            "GET",
            "PUT",
            "DELETE"
        ],
        "resource": "/apps/netflow/exporters/{alias}"
    },
    "appsnetflowexportersaliasfilter": {
        "methods": [
            "GET",
            "POST",
            "PUT",
            "DELETE"
        ],
        "resource": "/apps/netflow/exporters/{alias}/filter"
    },
    "appsnetflowexportersaliasfilterrules": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/netflow/exporters/{alias}/filter/rules"
    },
    "appsnetflowexportersaliasfilterrulesruleId": {
        "methods": [
            "DELETE"
        ],
        "resource": "/apps/netflow/exporters/{alias}/filter/rules/{ruleId}"
    },
    "appsnetflowmonitors": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/apps/netflow/monitors"
    },
    "appsnetflowmonitorsalias": {
        "methods": [
            "GET",
            "PUT",
            "DELETE"
        ],
        "resource": "/apps/netflow/monitors/{alias}"
    },
    "appsnetflowrecords": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/apps/netflow/records"
    },
    "appsnetflowrecordsalias": {
        "methods": [
            "GET",
            "PUT",
            "DELETE"
        ],
        "resource": "/apps/netflow/records/{alias}"
    },
    "appssaApfProfiles": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/apps/saApfProfiles"
    },
    "appssaApfProfilesalias": {
        "methods": [
            "GET",
            "PUT",
            "DELETE"
        ],
        "resource": "/apps/saApfProfiles/{alias}"
    },
    "appssaApfProfilesaliasfields": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/saApfProfiles/{alias}/fields"
    },
    "appssipwhitelists": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/apps/sip/whitelists"
    },
    "appssipwhitelistsalias": {
        "methods": [
            "DELETE"
        ],
        "resource": "/apps/sip/whitelists/{alias}"
    },
    "appssipwhitelistsaliasentries": {
        "methods": [
            "GET",
            "POST",
            "DELETE"
        ],
        "resource": "/apps/sip/whitelists/{alias}/entries"
    },
    "appssipwhitelistsaliasentriesall": {
        "methods": [
            "DELETE"
        ],
        "resource": "/apps/sip/whitelists/{alias}/entries/all"
    },
    "appssipwhitelistsaliasentriesfile": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/sip/whitelists/{alias}/entries/file"
    },
    "appssipwhitelistsaliasentriesremote": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/sip/whitelists/{alias}/entries/remote"
    },
    "appssslendpoints": {
        "methods": [
            "GET",
            "POST",
            "DELETE"
        ],
        "resource": "/apps/ssl/endpoints"
    },
    "appssslendpointsalias": {
        "methods": [
            "GET",
            "DELETE"
        ],
        "resource": "/apps/ssl/endpoints/{alias}"
    },
    "appssslkeyMaps": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/apps/ssl/keyMaps"
    },
    "appssslkeyMapsalias": {
        "methods": [
            "GET",
            "PUT",
            "DELETE"
        ],
        "resource": "/apps/ssl/keyMaps/{alias}"
    },
    "appssslkeyMapsaliasmappings": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/ssl/keyMaps/{alias}/mappings"
    },
    "appssslkeyMapsaliasmappingsendpointAlias": {
        "methods": [
            "DELETE"
        ],
        "resource": "/apps/ssl/keyMaps/{alias}/mappings/{endpointAlias}"
    },
    "appssslkeys": {
        "methods": [
            "GET",
            "POST",
            "DELETE"
        ],
        "resource": "/apps/ssl/keys"
    },
    "appssslkeysalias": {
        "methods": [
            "GET",
            "PATCH",
            "DELETE"
        ],
        "resource": "/apps/ssl/keys/{alias}"
    },
    "appssslkeysfile": {
        "methods": [
            "POST"
        ],
        "resource": "/apps/ssl/keys/file"
    },
    "appssslkeystore": {
        "methods": [
            "GET"
        ],
        "resource": "/apps/ssl/keystore"
    },
    "appssslkeystorelock": {
        "methods": [
            "PUT"
        ],
        "resource": "/apps/ssl/keystore/lock"
    },
    "appssslkeystorepassword": {
        "methods": [
            "POST",
            "PUT"
        ],
        "resource": "/apps/ssl/keystore/password"
    },
    "auditLog": {
        "methods": [
            "GET",
            "DELETE"
        ],
        "resource": "/auditLog"
    },
    "auditLogarchive": {
        "methods": [
            "POST"
        ],
        "resource": "/auditLog/archive"
    },
    "auditLogentryId": {
        "methods": [
            "GET"
        ],
        "resource": "/auditLog/{entryId}"
    },
    "avisipolicies": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/avisi/policies"
    },
    "avisipoliciesInstantiations": {
        "methods": [
            "GET"
        ],
        "resource": "/avisi/policiesInstantiations"
    },
    "avisipoliciesenable": {
        "methods": [
            "PUT"
        ],
        "resource": "/avisi/policies/enable"
    },
    "avisipoliciespolicyId": {
        "methods": [
            "GET",
            "PATCH",
            "PUT",
            "DELETE"
        ],
        "resource": "/avisi/policies/{policyId}"
    },
    "avisipoliciespolicyIdactions": {
        "methods": [
            "POST"
        ],
        "resource": "/avisi/policies/{policyId}/actions"
    },
    "avisipoliciespolicyIdactionsactionId": {
        "methods": [
            "DELETE"
        ],
        "resource": "/avisi/policies/{policyId}/actions/{actionId}"
    },
    "avisipoliciespolicyIdconditions": {
        "methods": [
            "POST"
        ],
        "resource": "/avisi/policies/{policyId}/conditions"
    },
    "avisipoliciespolicyIdconditionsconditionId": {
        "methods": [
            "DELETE"
        ],
        "resource": "/avisi/policies/{policyId}/conditions/{conditionId}"
    },
    "avisitemplatesactions": {
        "methods": [
            "GET"
        ],
        "resource": "/avisi/templates/actions"
    },
    "avisitemplatesconditions": {
        "methods": [
            "GET"
        ],
        "resource": "/avisi/templates/conditions"
    },
    "clusterConfigbackupdevicebackup": {
        "methods": [
            "POST"
        ],
        "resource": "/clusterConfig/backup/device/backup"
    },
    "clusterConfigbackupdevicenodeId": {
        "methods": [
            "GET",
            "PUT"
        ],
        "resource": "/clusterConfig/backup/device/{nodeId}"
    },
    "clusterConfigbackupdevicenodeIdconfigFileName": {
        "methods": [
            "DELETE"
        ],
        "resource": "/clusterConfig/backup/device/{nodeId}/{configFileName}"
    },
    "clusterConfigbackupfiledownloadclusterIdbackupId": {
        "methods": [
            "GET"
        ],
        "resource": "/clusterConfig/backup/file/download/{clusterId}/{backupId}"
    },
    "clusterConfigbackupfileupload": {
        "methods": [
            "POST"
        ],
        "resource": "/clusterConfig/backup/file/upload"
    },
    "clusterConfigbackuprepo": {
        "methods": [
            "GET"
        ],
        "resource": "/clusterConfig/backup/repo"
    },
    "clusterConfigbackuprepoclusterId": {
        "methods": [
            "GET",
            "PATCH",
            "DELETE"
        ],
        "resource": "/clusterConfig/backup/repo/{clusterId}"
    },
    "clusterConfigbackuprepoclusterIdbackupId": {
        "methods": [
            "DELETE"
        ],
        "resource": "/clusterConfig/backup/repo/{clusterId}/{backupId}"
    },
    "clusterConfigbackuprepoclusterIdrestore": {
        "methods": [
            "PUT"
        ],
        "resource": "/clusterConfig/backup/repo/{clusterId}/restore"
    },
    "clusterConfigbulkconfig": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/clusterConfig/bulk/config"
    },
    "clusterConfigbulkconfigdownloadfilename": {
        "methods": [
            "GET"
        ],
        "resource": "/clusterConfig/bulk/config/download/{filename}"
    },
    "clusterConfigbulkconfigfilename": {
        "methods": [
            "GET",
            "PATCH",
            "PUT",
            "DELETE"
        ],
        "resource": "/clusterConfig/bulk/config/{filename}"
    },
    "clusterConfigbulkconfigrestoreLogs": {
        "methods": [
            "GET"
        ],
        "resource": "/clusterConfig/bulk/config/restoreLogs"
    },
    "clusterConfigbulkconfigrestoreLogsconfigfilename": {
        "methods": [
            "GET"
        ],
        "resource": "/clusterConfig/bulk/config/restoreLogs/config/{filename}"
    },
    "clusterConfigbulkconfigrestoreLogsfilename": {
        "methods": [
            "GET",
            "DELETE"
        ],
        "resource": "/clusterConfig/bulk/config/restoreLogs/{filename}"
    },
    "clusterConfigimageUpgrade": {
        "methods": [
            "PUT"
        ],
        "resource": "/clusterConfig/imageUpgrade"
    },
    "clusterConfigreboot": {
        "methods": [
            "PUT"
        ],
        "resource": "/clusterConfig/reboot"
    },
    "events": {
        "methods": [
            "GET",
            "DELETE"
        ],
        "resource": "/events"
    },
    "eventsarchive": {
        "methods": [
            "POST"
        ],
        "resource": "/events/archive"
    },
    "eventseventId": {
        "methods": [
            "GET"
        ],
        "resource": "/events/{eventId}"
    },
    "eventsstatsaggregate": {
        "methods": [
            "GET"
        ],
        "resource": "/events/stats/aggregate"
    },
    "filterResources": {
        "methods": [
            "GET"
        ],
        "resource": "/filterResources"
    },
    "filterResourcesslotId": {
        "methods": [
            "GET"
        ],
        "resource": "/filterResources/{slotId}"
    },
    "filterTemplates": {
        "methods": [
            "GET",
            "POST",
            "DELETE"
        ],
        "resource": "/filterTemplates"
    },
    "filterTemplatesalias": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/filterTemplates/{alias}"
    },
    "filterTemplateslimitsall": {
        "methods": [
            "GET"
        ],
        "resource": "/filterTemplates/limits/all"
    },
    "filterTemplateslimitsslotId": {
        "methods": [
            "GET"
        ],
        "resource": "/filterTemplates/limits/{slotId}"
    },
    "filterTemplatesplatformlimits": {
        "methods": [
            "GET"
        ],
        "resource": "/filterTemplates/platform/limits"
    },
    "fmSystemarchiveServers": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/fmSystem/archiveServers"
    },
    "fmSystemarchiveServersserverAlias": {
        "methods": [
            "GET",
            "PUT",
            "DELETE"
        ],
        "resource": "/fmSystem/archiveServers/{serverAlias}"
    },
    "fmSystemarchiveServersserverAliasarchiveFiles": {
        "methods": [
            "GET"
        ],
        "resource": "/fmSystem/archiveServers/{serverAlias}/archiveFiles"
    },
    "fmSystembackup": {
        "methods": [
            "POST"
        ],
        "resource": "/fmSystem/backup"
    },
    "fmSystemimageUpgrade": {
        "methods": [
            "PUT"
        ],
        "resource": "/fmSystem/imageUpgrade"
    },
    "fmSystemreboot": {
        "methods": [
            "PUT"
        ],
        "resource": "/fmSystem/reboot"
    },
    "fmSystemrestore": {
        "methods": [
            "POST"
        ],
        "resource": "/fmSystem/restore"
    },
    "gdpcluster": {
        "methods": [
            "GET"
        ],
        "resource": "/gdp/cluster"
    },
    "gdpnode": {
        "methods": [
            "GET"
        ],
        "resource": "/gdp/node"
    },
    "gigasmartengine": {
        "methods": [
            "GET",
            "POST",
            "DELETE"
        ],
        "resource": "/gigasmart/engine"
    },
    "gigasmartenginearp": {
        "methods": [
            "GET"
        ],
        "resource": "/gigasmart/engine/arp"
    },
    "gigasmartengineeport": {
        "methods": [
            "GET",
            "DELETE"
        ],
        "resource": "/gigasmart/engine/{eport}"
    },
    "gigasmartengineeportarp": {
        "methods": [
            "GET"
        ],
        "resource": "/gigasmart/engine/{eport}/arp"
    },
    "gigasmartengineeportping": {
        "methods": [
            "GET"
        ],
        "resource": "/gigasmart/engine/{eport}/ping"
    },
    "gsGroups": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/gsGroups"
    },
    "gsGroupsalias": {
        "methods": [
            "GET",
            "DELETE"
        ],
        "resource": "/gsGroups/{alias}"
    },
    "gsGroupsaliasflowOpsReport": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/gsGroups/{alias}/flowOpsReport"
    },
    "gsGroupsaliasflowOpsReportflowFilteringsummary": {
        "methods": [
            "GET"
        ],
        "resource": "/gsGroups/{alias}/flowOpsReport/flowFiltering/summary"
    },
    "gsGroupsaliasflowOpsReportflowSamplingsummary": {
        "methods": [
            "GET"
        ],
        "resource": "/gsGroups/{alias}/flowOpsReport/flowSampling/summary"
    },
    "gsGroupsaliasflowOpsReportflowSipsummary": {
        "methods": [
            "GET"
        ],
        "resource": "/gsGroups/{alias}/flowOpsReport/flowSip/summary"
    },
    "gsGroupsaliasgtpPersistence": {
        "methods": [
            "GET"
        ],
        "resource": "/gsGroups/{alias}/gtpPersistence"
    },
    "gsGroupsaliasparams": {
        "methods": [
            "PUT",
            "PATCH"
        ],
        "resource": "/gsGroups/{alias}/params"
    },
    "gsGroupsaliasparamsdedup": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/dedup"
    },
    "gsGroupsaliasparamsengineWatchdogTimer": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/engineWatchdogTimer"
    },
    "gsGroupsaliasparamserspan3": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/erspan3"
    },
    "gsGroupsaliasparamsflowMask": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/flowMask"
    },
    "gsGroupsaliasparamsflowSampling": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/flowSampling"
    },
    "gsGroupsaliasparamsgenericSessionTimeout": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/genericSessionTimeout"
    },
    "gsGroupsaliasparamsgtpControlSampling": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/gtpControlSampling"
    },
    "gsGroupsaliasparamsgtpFlow": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/gtpFlow"
    },
    "gsGroupsaliasparamsgtpPersistence": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/gtpPersistence"
    },
    "gsGroupsaliasparamsgtpWhitelist": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/gtpWhitelist"
    },
    "gsGroupsaliasparamshealthCheck": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/healthCheck"
    },
    "gsGroupsaliasparamshsmGroup": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/hsmGroup"
    },
    "gsGroupsaliasparamsipFrag": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/ipFrag"
    },
    "gsGroupsaliasparamsloadBalance": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/loadBalance"
    },
    "gsGroupsaliasparamsnetflow": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/netflow"
    },
    "gsGroupsaliasparamsresource": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/resource"
    },
    "gsGroupsaliasparamsrtpPorts": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/rtpPorts"
    },
    "gsGroupsaliasparamssaApf": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/saApf"
    },
    "gsGroupsaliasparamssipMedia": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/sipMedia"
    },
    "gsGroupsaliasparamssipPorts": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/sipPorts"
    },
    "gsGroupsaliasparamssipSession": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/sipSession"
    },
    "gsGroupsaliasparamssipTcpIdleTimeout": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/sipTcpIdleTimeout"
    },
    "gsGroupsaliasparamssipWhitelist": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/sipWhitelist"
    },
    "gsGroupsaliasparamssslDecrypt": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/sslDecrypt"
    },
    "gsGroupsaliasparamssystem": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/system"
    },
    "gsGroupsaliasparamstunnelArpTimeout": {
        "methods": [
            "PUT"
        ],
        "resource": "/gsGroups/{alias}/params/tunnelArpTimeout"
    },
    "gsGroupsflowOpsReportflowFilteringsummary": {
        "methods": [
            "GET"
        ],
        "resource": "/gsGroups/flowOpsReport/flowFiltering/summary"
    },
    "gsGroupsflowOpsReportflowSamplingsummary": {
        "methods": [
            "GET"
        ],
        "resource": "/gsGroups/flowOpsReport/flowSampling/summary"
    },
    "gsGroupsflowOpsReportflowSipsummary": {
        "methods": [
            "GET"
        ],
        "resource": "/gsGroups/flowOpsReport/flowSip/summary"
    },
    "gsGroupsgtpPersistence": {
        "methods": [
            "GET"
        ],
        "resource": "/gsGroups/gtpPersistence"
    },
    "gsGroupsgtpPersistencefiles": {
        "methods": [
            "GET",
            "DELETE"
        ],
        "resource": "/gsGroups/gtpPersistence/files"
    },
    "gsGroupsgtpPersistencefilesfilename": {
        "methods": [
            "DELETE"
        ],
        "resource": "/gsGroups/gtpPersistence/files/{filename}"
    },
    "gsops": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/gsops"
    },
    "gsopsalias": {
        "methods": [
            "GET",
            "PUT",
            "DELETE"
        ],
        "resource": "/gsops/{alias}"
    },
    "gsopsaliasapps": {
        "methods": [
            "PATCH"
        ],
        "resource": "/gsops/{alias}/apps"
    },
    "healthStatusmaps": {
        "methods": [
            "GET"
        ],
        "resource": "/healthStatus/maps"
    },
    "imageServers": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/imageServers"
    },
    "imageServersalias": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/imageServers/{alias}"
    },
    "inlinehbPackets": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/inline/hbPackets"
    },
    "inlinehbPacketsalias": {
        "methods": [
            "GET",
            "DELETE"
        ],
        "resource": "/inline/hbPackets/{alias}"
    },
    "inlinehbPacketsfile": {
        "methods": [
            "POST"
        ],
        "resource": "/inline/hbPackets/file"
    },
    "inlinehbProfiles": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/inline/hbProfiles"
    },
    "inlinehbProfilesalias": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/inline/hbProfiles/{alias}"
    },
    "inlinehbProfilesaliasfile": {
        "methods": [
            "POST"
        ],
        "resource": "/inline/hbProfiles/{alias}/file"
    },
    "inlinenegativeHbProfiles": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/inline/negativeHbProfiles"
    },
    "inlinenegativeHbProfilesalias": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/inline/negativeHbProfiles/{alias}"
    },
    "inlinenegativeHbProfilesaliasfile": {
        "methods": [
            "POST"
        ],
        "resource": "/inline/negativeHbProfiles/{alias}/file"
    },
    "inlinenetworkGroups": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/inline/networkGroups"
    },
    "inlinenetworkGroupsalias": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/inline/networkGroups/{alias}"
    },
    "inlinenetworks": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/inline/networks"
    },
    "inlinenetworksalias": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/inline/networks/{alias}"
    },
    "inlineredundancyProfiles": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/inline/redundancyProfiles"
    },
    "inlineredundancyProfilesalias": {
        "methods": [
            "GET",
            "PATCH",
            "DELETE"
        ],
        "resource": "/inline/redundancyProfiles/{alias}"
    },
    "inlineserialToolGroups": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/inline/serialToolGroups"
    },
    "inlineserialToolGroupsalias": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/inline/serialToolGroups/{alias}"
    },
    "inlinetoolGroups": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/inline/toolGroups"
    },
    "inlinetoolGroupsalias": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/inline/toolGroups/{alias}"
    },
    "inlinetools": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/inline/tools"
    },
    "inlinetoolsalias": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/inline/tools/{alias}"
    },
    "inlinetoolsaliashbCounters": {
        "methods": [
            "DELETE"
        ],
        "resource": "/inline/tools/{alias}/hbCounters"
    },
    "inlinetoolsaliasnhbCounters": {
        "methods": [
            "DELETE"
        ],
        "resource": "/inline/tools/{alias}/nhbCounters"
    },
    "inlinetoolsaliasrecover": {
        "methods": [
            "PUT"
        ],
        "resource": "/inline/tools/{alias}/recover"
    },
    "inlinetoolshbCounters": {
        "methods": [
            "DELETE"
        ],
        "resource": "/inline/tools/hbCounters"
    },
    "inlinetoolsnhbCounters": {
        "methods": [
            "DELETE"
        ],
        "resource": "/inline/tools/nhbCounters"
    },
    "inventorychassis": {
        "methods": [
            "GET"
        ],
        "resource": "/inventory/chassis"
    },
    "inventorychassiscards": {
        "methods": [
            "GET"
        ],
        "resource": "/inventory/chassis/cards"
    },
    "inventorychassiscardsconfigure": {
        "methods": [
            "POST",
            "DELETE"
        ],
        "resource": "/inventory/chassis/cards/configure"
    },
    "inventorychassiscardsslotId": {
        "methods": [
            "GET",
            "PATCH"
        ],
        "resource": "/inventory/chassis/cards/{slotId}"
    },
    "inventorychassiscardsslotIdconfigure": {
        "methods": [
            "POST",
            "DELETE"
        ],
        "resource": "/inventory/chassis/cards/{slotId}/configure"
    },
    "inventorychassisconfigure": {
        "methods": [
            "POST",
            "PATCH",
            "DELETE"
        ],
        "resource": "/inventory/chassis/configure"
    },
    "inventoryports": {
        "methods": [
            "GET"
        ],
        "resource": "/inventory/ports"
    },
    "inventoryportsall": {
        "methods": [
            "GET"
        ],
        "resource": "/inventory/ports/all"
    },
    "inventoryportsneighbors": {
        "methods": [
            "GET"
        ],
        "resource": "/inventory/ports/neighbors"
    },
    "inventoryportsportId": {
        "methods": [
            "GET",
            "PATCH"
        ],
        "resource": "/inventory/ports/{portId}"
    },
    "licensingfm": {
        "methods": [
            "GET"
        ],
        "resource": "/licensing/fm"
    },
    "licensingfmlicenses": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/licensing/fm/licenses"
    },
    "licensingfmlicenseslicenseKey": {
        "methods": [
            "DELETE"
        ],
        "resource": "/licensing/fm/licenses/{licenseKey}"
    },
    "mapChains": {
        "methods": [
            "GET"
        ],
        "resource": "/mapChains"
    },
    "mapChainsaliases": {
        "methods": [
            "GET"
        ],
        "resource": "/mapChains/aliases"
    },
    "mapChainsaliasesmapChainId": {
        "methods": [
            "GET"
        ],
        "resource": "/mapChains/aliases/{mapChainId}"
    },
    "mapChainsmapChainId": {
        "methods": [
            "GET",
            "PUT"
        ],
        "resource": "/mapChains/{mapChainId}"
    },
    "mapChainsmapChainIdmapPriority": {
        "methods": [
            "PUT"
        ],
        "resource": "/mapChains/{mapChainId}/mapPriority"
    },
    "mapGroups": {
        "methods": [
            "GET",
            "POST",
            "DELETE"
        ],
        "resource": "/mapGroups"
    },
    "mapGroupsalias": {
        "methods": [
            "GET",
            "PUT",
            "DELETE"
        ],
        "resource": "/mapGroups/{alias}"
    },
    "mapTemplates": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/mapTemplates"
    },
    "mapTemplatesalias": {
        "methods": [
            "GET",
            "PUT",
            "DELETE"
        ],
        "resource": "/mapTemplates/{alias}"
    },
    "mapTemplatesaliasrules": {
        "methods": [
            "DELETE"
        ],
        "resource": "/mapTemplates/{alias}/rules"
    },
    "mapTemplatesaliasrulesruleId": {
        "methods": [
            "DELETE"
        ],
        "resource": "/mapTemplates/{alias}/rules/{ruleId}"
    },
    "mapTemplatesaliasrulesruleType": {
        "methods": [
            "POST"
        ],
        "resource": "/mapTemplates/{alias}/rules/{ruleType}"
    },
    "mapTemplatesaliasrulesruleTyperuleId": {
        "methods": [
            "PUT"
        ],
        "resource": "/mapTemplates/{alias}/rules/{ruleType}/{ruleId}"
    },
    "maps": {
        "methods": [
            "GET",
            "POST",
            "DELETE"
        ],
        "resource": "/maps"
    },
    "mapsalias": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/maps/{alias}"
    },
    "mapsaliasflowRules": {
        "methods": [
            "DELETE"
        ],
        "resource": "/maps/{alias}/flowRules"
    },
    "mapsaliasflowRulesruleId": {
        "methods": [
            "DELETE"
        ],
        "resource": "/maps/{alias}/flowRules/{ruleId}"
    },
    "mapsaliasflowRulesruleType": {
        "methods": [
            "POST"
        ],
        "resource": "/maps/{alias}/flowRules/{ruleType}"
    },
    "mapsaliasflowRulesruleTyperuleId": {
        "methods": [
            "PUT"
        ],
        "resource": "/maps/{alias}/flowRules/{ruleType}/{ruleId}"
    },
    "mapsaliasflowSampleOverlapRules": {
        "methods": [
            "DELETE"
        ],
        "resource": "/maps/{alias}/flowSampleOverlapRules"
    },
    "mapsaliasflowSampleOverlapRulespass": {
        "methods": [
            "POST"
        ],
        "resource": "/maps/{alias}/flowSampleOverlapRules/pass"
    },
    "mapsaliasflowSampleOverlapRulespassruleId": {
        "methods": [
            "PUT"
        ],
        "resource": "/maps/{alias}/flowSampleOverlapRules/pass/{ruleId}"
    },
    "mapsaliasflowSampleOverlapRulesruleId": {
        "methods": [
            "DELETE"
        ],
        "resource": "/maps/{alias}/flowSampleOverlapRules/{ruleId}"
    },
    "mapsaliasflowSampleRules": {
        "methods": [
            "DELETE"
        ],
        "resource": "/maps/{alias}/flowSampleRules"
    },
    "mapsaliasflowSampleRulespass": {
        "methods": [
            "POST"
        ],
        "resource": "/maps/{alias}/flowSampleRules/pass"
    },
    "mapsaliasflowSampleRulespassruleId": {
        "methods": [
            "PUT"
        ],
        "resource": "/maps/{alias}/flowSampleRules/pass/{ruleId}"
    },
    "mapsaliasflowSampleRulesruleId": {
        "methods": [
            "DELETE"
        ],
        "resource": "/maps/{alias}/flowSampleRules/{ruleId}"
    },
    "mapsaliasflowSampleSipRules": {
        "methods": [
            "DELETE"
        ],
        "resource": "/maps/{alias}/flowSampleSipRules"
    },
    "mapsaliasflowSampleSipRulespass": {
        "methods": [
            "POST"
        ],
        "resource": "/maps/{alias}/flowSampleSipRules/pass"
    },
    "mapsaliasflowSampleSipRulespassruleId": {
        "methods": [
            "PUT"
        ],
        "resource": "/maps/{alias}/flowSampleSipRules/pass/{ruleId}"
    },
    "mapsaliasflowSampleSipRulesruleId": {
        "methods": [
            "DELETE"
        ],
        "resource": "/maps/{alias}/flowSampleSipRules/{ruleId}"
    },
    "mapsaliasflowWhitelistOverlapRules": {
        "methods": [
            "DELETE"
        ],
        "resource": "/maps/{alias}/flowWhitelistOverlapRules"
    },
    "mapsaliasflowWhitelistOverlapRulespass": {
        "methods": [
            "POST"
        ],
        "resource": "/maps/{alias}/flowWhitelistOverlapRules/pass"
    },
    "mapsaliasflowWhitelistOverlapRulespassruleId": {
        "methods": [
            "PUT"
        ],
        "resource": "/maps/{alias}/flowWhitelistOverlapRules/pass/{ruleId}"
    },
    "mapsaliasflowWhitelistOverlapRulesruleId": {
        "methods": [
            "DELETE"
        ],
        "resource": "/maps/{alias}/flowWhitelistOverlapRules/{ruleId}"
    },
    "mapsaliasflowWhitelistRules": {
        "methods": [
            "DELETE",
            "DELETE"
        ],
        "resource": "/maps/{alias}/flowWhitelistRules"
    },
    "mapsaliasflowWhitelistRulespass": {
        "methods": [
            "POST",
            "POST"
        ],
        "resource": "/maps/{alias}/flowWhitelistRules/pass"
    },
    "mapsaliasflowWhitelistRulespassruleId": {
        "methods": [
            "PUT",
            "PUT"
        ],
        "resource": "/maps/{alias}/flowWhitelistRules/pass/{ruleId}"
    },
    "mapsaliasflowWhitelistRulesruleId": {
        "methods": [
            "DELETE",
            "DELETE"
        ],
        "resource": "/maps/{alias}/flowWhitelistRules/{ruleId}"
    },
    "mapsaliasgsRules": {
        "methods": [
            "DELETE"
        ],
        "resource": "/maps/{alias}/gsRules"
    },
    "mapsaliasgsRulesruleId": {
        "methods": [
            "DELETE"
        ],
        "resource": "/maps/{alias}/gsRules/{ruleId}"
    },
    "mapsaliasgsRulesruleType": {
        "methods": [
            "POST"
        ],
        "resource": "/maps/{alias}/gsRules/{ruleType}"
    },
    "mapsaliasgsRulesruleTyperuleId": {
        "methods": [
            "PUT"
        ],
        "resource": "/maps/{alias}/gsRules/{ruleType}/{ruleId}"
    },
    "mapsaliasrules": {
        "methods": [
            "DELETE"
        ],
        "resource": "/maps/{alias}/rules"
    },
    "mapsaliasrulesruleId": {
        "methods": [
            "DELETE"
        ],
        "resource": "/maps/{alias}/rules/{ruleId}"
    },
    "mapsaliasrulesruleType": {
        "methods": [
            "POST"
        ],
        "resource": "/maps/{alias}/rules/{ruleType}"
    },
    "mapsaliasrulesruleTyperuleId": {
        "methods": [
            "PUT"
        ],
        "resource": "/maps/{alias}/rules/{ruleType}/{ruleId}"
    },
    "mapsaliasrulestemplatetemplateAlias": {
        "methods": [
            "POST"
        ],
        "resource": "/maps/{alias}/rules/template/{templateAlias}"
    },
    "nodeCredentials": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/nodeCredentials"
    },
    "nodeCredentialsdeviceAddress": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/nodeCredentials/{deviceAddress}"
    },
    "nodes": {
        "methods": [
            "GET",
            "POST",
            "PUT",
            "DELETE"
        ],
        "resource": "/nodes"
    },
    "nodesflat": {
        "methods": [
            "GET"
        ],
        "resource": "/nodes/flat"
    },
    "portConfiggigastreams": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/portConfig/gigastreams"
    },
    "portConfiggigastreamsadvHashslotId": {
        "methods": [
            "GET",
            "PUT",
            "DELETE"
        ],
        "resource": "/portConfig/gigastreams/advHash/{slotId}"
    },
    "portConfiggigastreamsalias": {
        "methods": [
            "GET",
            "PATCH",
            "DELETE"
        ],
        "resource": "/portConfig/gigastreams/{alias}"
    },
    "portConfiggigastreamsaliashashIdshashBucketIds": {
        "methods": [
            "DELETE"
        ],
        "resource": "/portConfig/gigastreams/{alias}/hashIds/{hashBucketIds}"
    },
    "portConfigportConfigs": {
        "methods": [
            "GET"
        ],
        "resource": "/portConfig/portConfigs"
    },
    "portConfigportConfigsportId": {
        "methods": [
            "GET",
            "PUT",
            "PATCH"
        ],
        "resource": "/portConfig/portConfigs/{portId}"
    },
    "portConfigportGroups": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/portConfig/portGroups"
    },
    "portConfigportGroupsalias": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/portConfig/portGroups/{alias}"
    },
    "portConfigportPairs": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/portConfig/portPairs"
    },
    "portConfigportPairsalias": {
        "methods": [
            "GET",
            "PATCH",
            "DELETE"
        ],
        "resource": "/portConfig/portPairs/{alias}"
    },
    "portConfigstackLinks": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/portConfig/stackLinks"
    },
    "portConfigstackLinksalias": {
        "methods": [
            "GET",
            "DELETE"
        ],
        "resource": "/portConfig/stackLinks/{alias}"
    },
    "portConfigtoolPortFilters": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/portConfig/toolPortFilters"
    },
    "portConfigtoolPortFiltersportId": {
        "methods": [
            "GET",
            "DELETE"
        ],
        "resource": "/portConfig/toolPortFilters/{portId}"
    },
    "portConfigtoolPortFiltersportIdrulesruleId": {
        "methods": [
            "DELETE"
        ],
        "resource": "/portConfig/toolPortFilters/{portId}/rules/{ruleId}"
    },
    "portConfigtoolPortFiltersportIdrulesruleType": {
        "methods": [
            "POST"
        ],
        "resource": "/portConfig/toolPortFilters/{portId}/rules/{ruleType}"
    },
    "portConfigtoolPortFiltersportIdrulesruleTyperuleId": {
        "methods": [
            "PUT"
        ],
        "resource": "/portConfig/toolPortFilters/{portId}/rules/{ruleType}/{ruleId}"
    },
    "portConfigtoolPortMirrors": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/portConfig/toolPortMirrors"
    },
    "portConfigtoolPortMirrorsalias": {
        "methods": [
            "GET",
            "PATCH",
            "DELETE"
        ],
        "resource": "/portConfig/toolPortMirrors/{alias}"
    },
    "portConfigtunneledPorts": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/portConfig/tunneledPorts"
    },
    "portConfigtunneledPortsalias": {
        "methods": [
            "GET",
            "DELETE"
        ],
        "resource": "/portConfig/tunneledPorts/{alias}"
    },
    "portConfigtunneledPortsaliasgatewayMac": {
        "methods": [
            "DELETE"
        ],
        "resource": "/portConfig/tunneledPorts/{alias}/gatewayMac"
    },
    "portConfigtunneledPortsgatewayMacall": {
        "methods": [
            "DELETE"
        ],
        "resource": "/portConfig/tunneledPorts/gatewayMac/all"
    },
    "portConfigtunneledPortsgatewayMacipv4": {
        "methods": [
            "DELETE"
        ],
        "resource": "/portConfig/tunneledPorts/gatewayMac/ipv4"
    },
    "portConfigtunneledPortsgatewayMacipv6": {
        "methods": [
            "DELETE"
        ],
        "resource": "/portConfig/tunneledPorts/gatewayMac/ipv6"
    },
    "spineLinks": {
        "methods": [
            "GET"
        ],
        "resource": "/spineLinks"
    },
    "spineLinksalias": {
        "methods": [
            "GET"
        ],
        "resource": "/spineLinks/{alias}"
    },
    "systemaaaauth": {
        "methods": [
            "GET",
            "PUT",
            "PATCH"
        ],
        "resource": "/system/aaa/auth"
    },
    "systemaaaauthaccountLock": {
        "methods": [
            "DELETE"
        ],
        "resource": "/system/aaa/auth/accountLock"
    },
    "systemaaaauthservers": {
        "methods": [
            "GET",
            "PUT",
            "PATCH"
        ],
        "resource": "/system/aaa/auth/servers"
    },
    "systemaaaauthserversldap": {
        "methods": [
            "PUT"
        ],
        "resource": "/system/aaa/auth/servers/ldap"
    },
    "systemaaaauthserversradius": {
        "methods": [
            "PUT"
        ],
        "resource": "/system/aaa/auth/servers/radius"
    },
    "systemaaaauthserverstacacs": {
        "methods": [
            "PUT"
        ],
        "resource": "/system/aaa/auth/servers/tacacs"
    },
    "systemaaaroles": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/system/aaa/roles"
    },
    "systemaaarolesroleName": {
        "methods": [
            "PUT",
            "DELETE"
        ],
        "resource": "/system/aaa/roles/{roleName}"
    },
    "systemconfig": {
        "methods": [
            "POST"
        ],
        "resource": "/system/config"
    },
    "systemconfigactive": {
        "methods": [
            "GET"
        ],
        "resource": "/system/config/active"
    },
    "systemconfigfile": {
        "methods": [
            "POST"
        ],
        "resource": "/system/config/file"
    },
    "systemconfigfilefilename": {
        "methods": [
            "GET",
            "DELETE"
        ],
        "resource": "/system/config/file/{filename}"
    },
    "systemconfigfileimport": {
        "methods": [
            "POST"
        ],
        "resource": "/system/config/file/import"
    },
    "systemconfigfiles": {
        "methods": [
            "GET"
        ],
        "resource": "/system/config/files"
    },
    "systemconfigrevert": {
        "methods": [
            "POST"
        ],
        "resource": "/system/config/revert"
    },
    "systemconfigswitch": {
        "methods": [
            "POST"
        ],
        "resource": "/system/config/switch"
    },
    "systemconfigtraffic": {
        "methods": [
            "DELETE"
        ],
        "resource": "/system/config/traffic"
    },
    "systemdiag": {
        "methods": [
            "GET"
        ],
        "resource": "/system/diag"
    },
    "systememailnotifications": {
        "methods": [
            "GET",
            "PUT"
        ],
        "resource": "/system/email/notifications"
    },
    "systemeventNotificationconfigdeviceIp": {
        "methods": [
            "PUT"
        ],
        "resource": "/system/eventNotification/config/{deviceIp}"
    },
    "systemeventNotificationtargets": {
        "methods": [
            "GET"
        ],
        "resource": "/system/eventNotification/targets"
    },
    "systeminterfaces": {
        "methods": [
            "GET"
        ],
        "resource": "/system/interfaces"
    },
    "systemldapServers": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/system/ldapServers"
    },
    "systemldapServersserverAddress": {
        "methods": [
            "DELETE"
        ],
        "resource": "/system/ldapServers/{serverAddress}"
    },
    "systemlocalUsers": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/system/localUsers"
    },
    "systemlocalUsersusername": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/system/localUsers/{username}"
    },
    "systemradiusServers": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/system/radiusServers"
    },
    "systemradiusServersserverAddress": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/system/radiusServers/{serverAddress}"
    },
    "systemsecurity": {
        "methods": [
            "GET",
            "PUT",
            "PATCH"
        ],
        "resource": "/system/security"
    },
    "systemsnmp": {
        "methods": [
            "GET"
        ],
        "resource": "/system/snmp"
    },
    "systemsnmpcommunity": {
        "methods": [
            "PUT",
            "PATCH"
        ],
        "resource": "/system/snmp/community"
    },
    "systemsnmpnotifTargets": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/system/snmp/notifTargets"
    },
    "systemsnmpnotifTargetsnotifTargetAddress": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/system/snmp/notifTargets/{notifTargetAddress}"
    },
    "systemsnmpnotifications": {
        "methods": [
            "PUT",
            "PATCH"
        ],
        "resource": "/system/snmp/notifications"
    },
    "systemsnmpsystem": {
        "methods": [
            "PUT",
            "PATCH"
        ],
        "resource": "/system/snmp/system"
    },
    "systemsnmpv3Users": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/system/snmp/v3Users"
    },
    "systemsnmpv3UsersuserName": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/system/snmp/v3Users/{userName}"
    },
    "systemsysdump": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/system/sysdump"
    },
    "systemsysdumpfilefilename": {
        "methods": [
            "GET"
        ],
        "resource": "/system/sysdump/file/{filename}"
    },
    "systemsysdumpfilename": {
        "methods": [
            "DELETE"
        ],
        "resource": "/system/sysdump/{filename}"
    },
    "systemsyslog": {
        "methods": [
            "GET",
            "DELETE"
        ],
        "resource": "/system/syslog"
    },
    "systemsyslogarchive": {
        "methods": [
            "POST"
        ],
        "resource": "/system/syslog/archive"
    },
    "systemsyslogconfig": {
        "methods": [
            "GET"
        ],
        "resource": "/system/syslog/config"
    },
    "systemsyslogconfigclusterId": {
        "methods": [
            "PUT",
            "PATCH"
        ],
        "resource": "/system/syslog/config/{clusterId}"
    },
    "systemtacacsServers": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/system/tacacsServers"
    },
    "systemtacacsServersserverAddress": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/system/tacacsServers/{serverAddress}"
    },
    "systemtimeclock": {
        "methods": [
            "GET",
            "PUT"
        ],
        "resource": "/system/time/clock"
    },
    "systemtimentp": {
        "methods": [
            "GET",
            "PUT",
            "PATCH"
        ],
        "resource": "/system/time/ntp"
    },
    "systemtimentpauthKeys": {
        "methods": [
            "POST"
        ],
        "resource": "/system/time/ntp/authKeys"
    },
    "systemtimentpauthKeysauthKeyId": {
        "methods": [
            "DELETE"
        ],
        "resource": "/system/time/ntp/authKeys/{authKeyId}"
    },
    "systemtimentpservers": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/system/time/ntp/servers"
    },
    "systemtimentpserversserverAddress": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/system/time/ntp/servers/{serverAddress}"
    },
    "systemtimentpsync": {
        "methods": [
            "PUT"
        ],
        "resource": "/system/time/ntp/sync"
    },
    "systemtimeppsSource": {
        "methods": [
            "GET",
            "PUT"
        ],
        "resource": "/system/time/ppsSource"
    },
    "systemtimeptp": {
        "methods": [
            "GET",
            "PUT"
        ],
        "resource": "/system/time/ptp"
    },
    "systemuboot": {
        "methods": [
            "POST"
        ],
        "resource": "/system/uboot"
    },
    "topology": {
        "methods": [
            "GET"
        ],
        "resource": "/topology"
    },
    "topologymanual": {
        "methods": [
            "DELETE"
        ],
        "resource": "/topology/manual"
    },
    "topologymanuallinks": {
        "methods": [
            "POST"
        ],
        "resource": "/topology/manual/links"
    },
    "topologymanuallinkstopoLinkId": {
        "methods": [
            "DELETE"
        ],
        "resource": "/topology/manual/links/{topoLinkId}"
    },
    "topologymanualnodes": {
        "methods": [
            "POST"
        ],
        "resource": "/topology/manual/nodes"
    },
    "topologymanualnodestopoNodeId": {
        "methods": [
            "PUT",
            "DELETE"
        ],
        "resource": "/topology/manual/nodes/{topoNodeId}"
    },
    "trafficAnalyzerappstimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trafficAnalyzer/apps/timeSeries"
    },
    "trafficAnalyzerappstop": {
        "methods": [
            "GET"
        ],
        "resource": "/trafficAnalyzer/apps/top"
    },
    "trafficAnalyzerconversations": {
        "methods": [
            "GET"
        ],
        "resource": "/trafficAnalyzer/conversations"
    },
    "trafficAnalyzerconversationstimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trafficAnalyzer/conversations/timeSeries"
    },
    "trafficAnalyzerconversationstop": {
        "methods": [
            "GET"
        ],
        "resource": "/trafficAnalyzer/conversations/top"
    },
    "trafficAnalyzerendpointstimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trafficAnalyzer/endpoints/timeSeries"
    },
    "trafficAnalyzerendpointstop": {
        "methods": [
            "GET"
        ],
        "resource": "/trafficAnalyzer/endpoints/top"
    },
    "trafficAnalyzerexternalInterfaces": {
        "methods": [
            "GET"
        ],
        "resource": "/trafficAnalyzer/externalInterfaces"
    },
    "trafficAnalyzerexternalInterfacestimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trafficAnalyzer/externalInterfaces/timeSeries"
    },
    "trafficAnalyzerexternalInterfacestop": {
        "methods": [
            "GET"
        ],
        "resource": "/trafficAnalyzer/externalInterfaces/top"
    },
    "trafficAnalyzerinterfaces": {
        "methods": [
            "GET"
        ],
        "resource": "/trafficAnalyzer/interfaces"
    },
    "trafficAnalyzerinterfacestimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trafficAnalyzer/interfaces/timeSeries"
    },
    "trafficAnalyzerinterfacestop": {
        "methods": [
            "GET"
        ],
        "resource": "/trafficAnalyzer/interfaces/top"
    },
    "trafficAnalyzerprotocolstimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trafficAnalyzer/protocols/timeSeries"
    },
    "trafficAnalyzerprotocolstop": {
        "methods": [
            "GET"
        ],
        "resource": "/trafficAnalyzer/protocols/top"
    },
    "trafficAnalyzerurls": {
        "methods": [
            "GET"
        ],
        "resource": "/trafficAnalyzer/urls"
    },
    "trafficAnalyzerurlstimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trafficAnalyzer/urls/timeSeries"
    },
    "trafficAnalyzerurlstop": {
        "methods": [
            "GET"
        ],
        "resource": "/trafficAnalyzer/urls/top"
    },
    "trending": {
        "methods": [
            "DELETE"
        ],
        "resource": "/trending"
    },
    "trendinggsEnginetimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trending/gsEngine/timeSeries"
    },
    "trendinggsGroupstimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trending/gsGroups/timeSeries"
    },
    "trendinggsopstimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trending/gsops/timeSeries"
    },
    "trendinggvmMapstimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trending/gvmMaps/timeSeries"
    },
    "trendinggvmPortstimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trending/gvmPorts/timeSeries"
    },
    "trendingmapstimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trending/maps/timeSeries"
    },
    "trendingnetflowGeneratorexporterstimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trending/netflowGenerator/exporters/timeSeries"
    },
    "trendingnetflowGeneratormonitorstimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trending/netflowGenerator/monitors/timeSeries"
    },
    "trendingportGroupLbstimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trending/portGroupLbs/timeSeries"
    },
    "trendingportstimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trending/ports/timeSeries"
    },
    "trendingtunneledPortstimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trending/tunneledPorts/timeSeries"
    },
    "trendingvportstimeSeries": {
        "methods": [
            "GET"
        ],
        "resource": "/trending/vports/timeSeries"
    },
    "tunnelEndpoints": {
        "methods": [
            "GET"
        ],
        "resource": "/tunnelEndpoints"
    },
    "tunnelLbEndpoints": {
        "methods": [
            "GET",
            "POST",
            "DELETE"
        ],
        "resource": "/tunnelLbEndpoints"
    },
    "tunnelLbEndpointsteId": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/tunnelLbEndpoints/{teId}"
    },
    "vports": {
        "methods": [
            "GET",
            "POST"
        ],
        "resource": "/vports"
    },
    "vportsalias": {
        "methods": [
            "GET",
            "PUT",
            "PATCH",
            "DELETE"
        ],
        "resource": "/vports/{alias}"
    }
}

RESOURCE_MAPPING_v09 = {
    "login": {
        "methods": [
            "POST"
        ],
        "resource": "/login"
    },
    "logout": {
        "methods": [
            "DELETE"
        ],
        "resource": "/logout"
    },
    "sysinfo": {
        "methods": [
            "GET"
        ],
        "resource": "/sys/info"
    },
    "user": {
        "methods": [
            "POST"
        ],
        "resource": "/sys/user"
    }
}

