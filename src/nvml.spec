# @ stub nvmlComputeInstanceDestroy
# @ stub nvmlComputeInstanceGetInfo
# @ stub nvmlComputeInstanceGetInfo_v2
# @ stub nvmlDeviceClearAccountingPids
@ cdecl nvmlDeviceClearCpuAffinity(ptr)
# @ stub nvmlDeviceClearEccErrorCounts
# @ stub nvmlDeviceCreateGpuInstance
# @ stub nvmlDeviceCreateGpuInstanceWithPlacement
@ cdecl nvmlDeviceDiscoverGpus(ptr)
# @ stub nvmlDeviceFreezeNvLinkUtilizationCounter
# @ stub nvmlDeviceGetAPIRestriction
# @ stub nvmlDeviceGetAccountingBufferSize
# @ stub nvmlDeviceGetAccountingMode
# @ stub nvmlDeviceGetAccountingPids
# @ stub nvmlDeviceGetAccountingStats
# @ stub nvmlDeviceGetActiveVgpus
# @ stub nvmlDeviceGetApplicationsClock
# @ stub nvmlDeviceGetArchitecture
# @ stub nvmlDeviceGetAttributes
# @ stub nvmlDeviceGetAttributes_v2
# @ stub nvmlDeviceGetAutoBoostedClocksEnabled
# @ stub nvmlDeviceGetBAR1MemoryInfo
# @ stub nvmlDeviceGetBoardId
# @ stub nvmlDeviceGetBoardPartNumber
# @ stub nvmlDeviceGetBrand
# @ stub nvmlDeviceGetBridgeChipInfo
@ cdecl nvmlDeviceGetClock(ptr long long ptr)
# @ stub nvmlDeviceGetClockInfo
# @ stub nvmlDeviceGetComputeInstanceId
@ cdecl nvmlDeviceGetComputeMode(ptr ptr)
# @ stub nvmlDeviceGetComputeRunningProcesses
# @ stub nvmlDeviceGetComputeRunningProcesses_v2
# @ stub nvmlDeviceGetCount
@ cdecl nvmlDeviceGetCount_v2(ptr)
@ cdecl nvmlDeviceGetCpuAffinity(ptr long ptr)
@ cdecl nvmlDeviceGetCpuAffinityWithinScope(ptr long ptr long)
# @ stub nvmlDeviceGetCreatableVgpus
# @ stub nvmlDeviceGetCudaComputeCapability
# @ stub nvmlDeviceGetCurrPcieLinkGeneration
@ cdecl nvmlDeviceGetCurrPcieLinkWidth(ptr ptr)
@ cdecl nvmlDeviceGetCurrentClocksThrottleReasons(ptr ptr)
@ cdecl nvmlDeviceGetDecoderUtilization(ptr ptr ptr)
# @ stub nvmlDeviceGetDefaultApplicationsClock
# @ stub nvmlDeviceGetDetailedEccErrors
# @ stub nvmlDeviceGetDeviceHandleFromMigDeviceHandle
# @ stub nvmlDeviceGetDisplayActive
# @ stub nvmlDeviceGetDisplayMode
@ cdecl nvmlDeviceGetDriverModel(ptr ptr ptr)
# @ stub nvmlDeviceGetEccMode
# @ stub nvmlDeviceGetEncoderCapacity
# @ stub nvmlDeviceGetEncoderSessions
# @ stub nvmlDeviceGetEncoderStats
@ cdecl nvmlDeviceGetEncoderUtilization(ptr ptr ptr)
@ cdecl nvmlDeviceGetEnforcedPowerLimit(ptr ptr)
# @ stub nvmlDeviceGetFBCSessions
# @ stub nvmlDeviceGetFBCStats
# @ stub nvmlDeviceGetFanSpeed
@ cdecl nvmlDeviceGetFanSpeed_v2(ptr long ptr)
# @ stub nvmlDeviceGetFieldValues
# @ stub nvmlDeviceGetGpuInstanceById
# @ stub nvmlDeviceGetGpuInstanceId
# @ stub nvmlDeviceGetGpuInstancePossiblePlacements
# @ stub nvmlDeviceGetGpuInstanceProfileInfo
# @ stub nvmlDeviceGetGpuInstanceRemainingCapacity
# @ stub nvmlDeviceGetGpuInstances
# @ stub nvmlDeviceGetGpuOperationMode
# @ stub nvmlDeviceGetGraphicsRunningProcesses
# @ stub nvmlDeviceGetGraphicsRunningProcesses_v2
# @ stub nvmlDeviceGetGridLicensableFeatures
# @ stub nvmlDeviceGetGridLicensableFeatures_v2
# @ stub nvmlDeviceGetGridLicensableFeatures_v3
@ cdecl nvmlDeviceGetHandleByIndex(long ptr)
@ cdecl nvmlDeviceGetHandleByIndex_v2(long ptr)
@ cdecl nvmlDeviceGetHandleByPciBusId(str ptr)
@ cdecl nvmlDeviceGetHandleByPciBusId_v2(str ptr)
@ cdecl nvmlDeviceGetHandleBySerial(str ptr)
@ cdecl nvmlDeviceGetHandleByUUID(str ptr)
# @ stub nvmlDeviceGetHostVgpuMode
@ cdecl nvmlDeviceGetIndex(ptr ptr)
# @ stub nvmlDeviceGetInforomConfigurationChecksum
# @ stub nvmlDeviceGetInforomImageVersion
# @ stub nvmlDeviceGetInforomVersion
# @ stub nvmlDeviceGetMPSComputeRunningProcesses
# @ stub nvmlDeviceGetMaxClockInfo
# @ stub nvmlDeviceGetMaxCustomerBoostClock
# @ stub nvmlDeviceGetMaxMigDeviceCount
# @ stub nvmlDeviceGetMaxPcieLinkGeneration
# @ stub nvmlDeviceGetMaxPcieLinkWidth
@ cdecl nvmlDeviceGetMemoryAffinity(ptr long ptr long)
# @ stub nvmlDeviceGetMemoryErrorCounter
@ cdecl nvmlDeviceGetMemoryInfo(ptr ptr)
# @ stub nvmlDeviceGetMigDeviceHandleByIndex
# @ stub nvmlDeviceGetMigMode
@ cdecl nvmlDeviceGetMinorNumber(ptr ptr)
# @ stub nvmlDeviceGetMultiGpuBoard
@ cdecl nvmlDeviceGetName(ptr str long)
# @ stub nvmlDeviceGetNvLinkCapability
# @ stub nvmlDeviceGetNvLinkErrorCounter
# @ stub nvmlDeviceGetNvLinkRemotePciInfo
# @ stub nvmlDeviceGetNvLinkRemotePciInfo_v2
# @ stub nvmlDeviceGetNvLinkState
# @ stub nvmlDeviceGetNvLinkUtilizationControl
# @ stub nvmlDeviceGetNvLinkUtilizationCounter
# @ stub nvmlDeviceGetNvLinkVersion
# @ stub nvmlDeviceGetP2PStatus
@ cdecl nvmlDeviceGetPciInfo(ptr ptr)
@ cdecl nvmlDeviceGetPciInfo_v2(ptr ptr)
@ cdecl nvmlDeviceGetPciInfo_v3(ptr ptr)
# @ stub nvmlDeviceGetPcieReplayCounter
# @ stub nvmlDeviceGetPcieThroughput
@ cdecl nvmlDeviceGetPerformanceState(ptr ptr)
@ cdecl nvmlDeviceGetPersistenceMode(ptr ptr)
# @ stub nvmlDeviceGetPgpuMetadataString
# @ stub nvmlDeviceGetPowerManagementDefaultLimit
# @ stub nvmlDeviceGetPowerManagementLimit
# @ stub nvmlDeviceGetPowerManagementLimitConstraints
# @ stub nvmlDeviceGetPowerManagementMode
# @ stub nvmlDeviceGetPowerState
@ cdecl nvmlDeviceGetPowerUsage(ptr ptr)
# @ stub nvmlDeviceGetProcessUtilization
# @ stub nvmlDeviceGetRemappedRows
# @ stub nvmlDeviceGetRetiredPages
# @ stub nvmlDeviceGetRetiredPagesPendingStatus
# @ stub nvmlDeviceGetRetiredPages_v2
# @ stub nvmlDeviceGetRowRemapperHistogram
# @ stub nvmlDeviceGetSamples
@ cdecl nvmlDeviceGetSerial(ptr str long)
# @ stub nvmlDeviceGetSupportedClocksThrottleReasons
# @ stub nvmlDeviceGetSupportedEventTypes
# @ stub nvmlDeviceGetSupportedGraphicsClocks
# @ stub nvmlDeviceGetSupportedMemoryClocks
# @ stub nvmlDeviceGetSupportedVgpus
@ cdecl nvmlDeviceGetTemperature(ptr long ptr)
@ cdecl nvmlDeviceGetTemperatureThreshold(ptr long ptr)
@ cdecl nvmlDeviceGetTopologyCommonAncestor(ptr ptr ptr)
@ cdecl nvmlDeviceGetTopologyNearestGpus(ptr long ptr ptr)
# @ stub nvmlDeviceGetTotalEccErrors
# @ stub nvmlDeviceGetTotalEnergyConsumption
@ cdecl nvmlDeviceGetUUID(ptr str long)
@ cdecl nvmlDeviceGetUtilizationRates(ptr ptr)
@ cdecl nvmlDeviceGetVbiosVersion(ptr str long)
# @ stub nvmlDeviceGetVgpuMetadata
# @ stub nvmlDeviceGetVgpuProcessUtilization
# @ stub nvmlDeviceGetVgpuUtilization
# @ stub nvmlDeviceGetViolationStatus
# @ stub nvmlDeviceGetVirtualizationMode
# @ stub nvmlDeviceIsMigDeviceHandle
@ cdecl nvmlDeviceModifyDrainState(ptr long)
# @ stub nvmlDeviceOnSameBoard
@ cdecl nvmlDeviceQueryDrainState(ptr ptr)
# @ stub nvmlDeviceRegisterEvents
# @ stub nvmlDeviceRemoveGpu
@ cdecl nvmlDeviceRemoveGpu_v2(ptr long long)
# @ stub nvmlDeviceResetApplicationsClocks
# @ stub nvmlDeviceResetGpuLockedClocks
# @ stub nvmlDeviceResetMemoryLockedClocks
# @ stub nvmlDeviceResetNvLinkErrorCounters
# @ stub nvmlDeviceResetNvLinkUtilizationCounter
# @ stub nvmlDeviceSetAPIRestriction
# @ stub nvmlDeviceSetAccountingMode
# @ stub nvmlDeviceSetApplicationsClocks
# @ stub nvmlDeviceSetAutoBoostedClocksEnabled
@ cdecl nvmlDeviceSetComputeMode(ptr long)
@ cdecl nvmlDeviceSetCpuAffinity(ptr)
# @ stub nvmlDeviceSetDefaultAutoBoostedClocksEnabled
@ cdecl nvmlDeviceSetDriverModel(ptr long long)
# @ stub nvmlDeviceSetEccMode
# @ stub nvmlDeviceSetGpuLockedClocks
# @ stub nvmlDeviceSetGpuOperationMode
# @ stub nvmlDeviceSetMemoryLockedClocks
# @ stub nvmlDeviceSetMigMode
# @ stub nvmlDeviceSetNvLinkUtilizationControl
@ cdecl nvmlDeviceSetPersistenceMode(ptr long)
# @ stub nvmlDeviceSetPowerManagementLimit
# @ stub nvmlDeviceSetTemperatureThreshold
# @ stub nvmlDeviceSetVirtualizationMode
# @ stub nvmlDeviceValidateInforom
@ cdecl nvmlErrorString(long)
# @ stub nvmlEventSetCreate
# @ stub nvmlEventSetFree
# @ stub nvmlEventSetWait
# @ stub nvmlEventSetWait_v2
# @ stub nvmlGetBlacklistDeviceCount
# @ stub nvmlGetBlacklistDeviceInfoByIndex
# @ stub nvmlGetExcludedDeviceCount
# @ stub nvmlGetExcludedDeviceInfoByIndex
# @ stub nvmlGetVgpuCompatibility
# @ stub nvmlGetVgpuVersion
# @ stub nvmlGpuInstanceCreateComputeInstance
# @ stub nvmlGpuInstanceDestroy
# @ stub nvmlGpuInstanceGetComputeInstanceById
# @ stub nvmlGpuInstanceGetComputeInstanceProfileInfo
# @ stub nvmlGpuInstanceGetComputeInstanceRemainingCapacity
# @ stub nvmlGpuInstanceGetComputeInstances
# @ stub nvmlGpuInstanceGetInfo
# @ stub nvmlInit
@ cdecl nvmlInitWithFlags(long)
@ cdecl nvmlInit_v2()
@ cdecl nvmlInternalGetExportTable(ptr ptr)
# @ stub nvmlSetVgpuVersion
@ cdecl nvmlShutdown()
@ cdecl nvmlSystemGetCudaDriverVersion(ptr)
@ cdecl nvmlSystemGetCudaDriverVersion_v2(ptr)
@ cdecl nvmlSystemGetDriverVersion(str long)
# @ stub nvmlSystemGetHicVersion
@ cdecl nvmlSystemGetNVMLVersion(str long)
# @ stub nvmlSystemGetProcessName
@ cdecl nvmlSystemGetTopologyGpuSet(long ptr ptr)
# @ stub nvmlUnitGetCount
# @ stub nvmlUnitGetDevices
# @ stub nvmlUnitGetFanSpeedInfo
# @ stub nvmlUnitGetHandleByIndex
# @ stub nvmlUnitGetLedState
# @ stub nvmlUnitGetPsuInfo
# @ stub nvmlUnitGetTemperature
# @ stub nvmlUnitGetUnitInfo
# @ stub nvmlUnitSetLedState
# @ stub nvmlVgpuInstanceClearAccountingPids
# @ stub nvmlVgpuInstanceGetAccountingMode
# @ stub nvmlVgpuInstanceGetAccountingPids
# @ stub nvmlVgpuInstanceGetAccountingStats
# @ stub nvmlVgpuInstanceGetEccMode
# @ stub nvmlVgpuInstanceGetEncoderCapacity
# @ stub nvmlVgpuInstanceGetEncoderSessions
# @ stub nvmlVgpuInstanceGetEncoderStats
# @ stub nvmlVgpuInstanceGetFBCSessions
# @ stub nvmlVgpuInstanceGetFBCStats
# @ stub nvmlVgpuInstanceGetFbUsage
# @ stub nvmlVgpuInstanceGetFrameRateLimit
# @ stub nvmlVgpuInstanceGetGpuInstanceId
# @ stub nvmlVgpuInstanceGetLicenseStatus
# @ stub nvmlVgpuInstanceGetMdevUUID
# @ stub nvmlVgpuInstanceGetMetadata
# @ stub nvmlVgpuInstanceGetType
# @ stub nvmlVgpuInstanceGetUUID
# @ stub nvmlVgpuInstanceGetVmDriverVersion
# @ stub nvmlVgpuInstanceGetVmID
# @ stub nvmlVgpuInstanceSetEncoderCapacity
# @ stub nvmlVgpuTypeGetClass
# @ stub nvmlVgpuTypeGetDeviceID
# @ stub nvmlVgpuTypeGetFrameRateLimit
# @ stub nvmlVgpuTypeGetFramebufferSize
# @ stub nvmlVgpuTypeGetGpuInstanceProfileId
# @ stub nvmlVgpuTypeGetLicense
# @ stub nvmlVgpuTypeGetMaxInstances
# @ stub nvmlVgpuTypeGetMaxInstancesPerVm
# @ stub nvmlVgpuTypeGetName
# @ stub nvmlVgpuTypeGetNumDisplayHeads
# @ stub nvmlVgpuTypeGetResolution