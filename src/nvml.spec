@ stub nvmlComputeInstanceDestroy
@ stub nvmlComputeInstanceGetInfo
@ stub nvmlComputeInstanceGetInfo_v2
@ stub nvmlDeviceClearAccountingPids
@ stub nvmlDeviceClearCpuAffinity
@ stub nvmlDeviceClearEccErrorCounts
@ stub nvmlDeviceCreateGpuInstance
@ stub nvmlDeviceCreateGpuInstanceWithPlacement
@ stub nvmlDeviceDiscoverGpus
@ stub nvmlDeviceFreezeNvLinkUtilizationCounter
@ stub nvmlDeviceGetAPIRestriction
@ stub nvmlDeviceGetAccountingBufferSize
@ stub nvmlDeviceGetAccountingMode
@ stub nvmlDeviceGetAccountingPids
@ stub nvmlDeviceGetAccountingStats
@ stub nvmlDeviceGetActiveVgpus
@ stub nvmlDeviceGetApplicationsClock
@ stub nvmlDeviceGetArchitecture
@ stub nvmlDeviceGetAttributes
@ stub nvmlDeviceGetAttributes_v2
@ stub nvmlDeviceGetAutoBoostedClocksEnabled
@ stub nvmlDeviceGetBAR1MemoryInfo
@ stub nvmlDeviceGetBoardId
@ stub nvmlDeviceGetBoardPartNumber
@ stub nvmlDeviceGetBrand
@ stub nvmlDeviceGetBridgeChipInfo
@ stdcall nvmlDeviceGetClock(ptr long long ptr)
@ stub nvmlDeviceGetClockInfo
@ stub nvmlDeviceGetComputeInstanceId
@ stdcall nvmlDeviceGetComputeMode(ptr ptr)
@ stub nvmlDeviceGetComputeRunningProcesses
@ stub nvmlDeviceGetComputeRunningProcesses_v2
@ stub nvmlDeviceGetCount
@ stdcall nvmlDeviceGetCount_v2(ptr)
@ stub nvmlDeviceGetCpuAffinity
@ stub nvmlDeviceGetCpuAffinityWithinScope
@ stub nvmlDeviceGetCreatableVgpus
@ stub nvmlDeviceGetCudaComputeCapability
@ stub nvmlDeviceGetCurrPcieLinkGeneration
@ stdcall nvmlDeviceGetCurrPcieLinkWidth(ptr ptr)
@ stdcall nvmlDeviceGetCurrentClocksThrottleReasons(ptr ptr)
@ stub nvmlDeviceGetDecoderUtilization
@ stub nvmlDeviceGetDefaultApplicationsClock
@ stub nvmlDeviceGetDetailedEccErrors
@ stub nvmlDeviceGetDeviceHandleFromMigDeviceHandle
@ stub nvmlDeviceGetDisplayActive
@ stub nvmlDeviceGetDisplayMode
@ stub nvmlDeviceGetDriverModel
@ stub nvmlDeviceGetEccMode
@ stub nvmlDeviceGetEncoderCapacity
@ stub nvmlDeviceGetEncoderSessions
@ stub nvmlDeviceGetEncoderStats
@ stub nvmlDeviceGetEncoderUtilization
@ stdcall nvmlDeviceGetEnforcedPowerLimit(ptr ptr)
@ stub nvmlDeviceGetFBCSessions
@ stub nvmlDeviceGetFBCStats
@ stub nvmlDeviceGetFanSpeed
@ stdcall nvmlDeviceGetFanSpeed_v2(ptr long ptr)
@ stub nvmlDeviceGetFieldValues
@ stub nvmlDeviceGetGpuInstanceById
@ stub nvmlDeviceGetGpuInstanceId
@ stub nvmlDeviceGetGpuInstancePossiblePlacements
@ stub nvmlDeviceGetGpuInstanceProfileInfo
@ stub nvmlDeviceGetGpuInstanceRemainingCapacity
@ stub nvmlDeviceGetGpuInstances
@ stub nvmlDeviceGetGpuOperationMode
@ stub nvmlDeviceGetGraphicsRunningProcesses
@ stub nvmlDeviceGetGraphicsRunningProcesses_v2
@ stub nvmlDeviceGetGridLicensableFeatures
@ stub nvmlDeviceGetGridLicensableFeatures_v2
@ stub nvmlDeviceGetGridLicensableFeatures_v3
@ stdcall nvmlDeviceGetHandleByIndex(long ptr)
@ stdcall nvmlDeviceGetHandleByIndex_v2(long ptr)
@ stdcall nvmlDeviceGetHandleByPciBusId(str ptr)
@ stdcall nvmlDeviceGetHandleByPciBusId_v2(str ptr)
@ stdcall nvmlDeviceGetHandleBySerial(str ptr)
@ stdcall nvmlDeviceGetHandleByUUID(str ptr)
@ stub nvmlDeviceGetHostVgpuMode
@ stdcall nvmlDeviceGetIndex(ptr ptr)
@ stub nvmlDeviceGetInforomConfigurationChecksum
@ stub nvmlDeviceGetInforomImageVersion
@ stub nvmlDeviceGetInforomVersion
@ stub nvmlDeviceGetMPSComputeRunningProcesses
@ stub nvmlDeviceGetMaxClockInfo
@ stub nvmlDeviceGetMaxCustomerBoostClock
@ stub nvmlDeviceGetMaxMigDeviceCount
@ stub nvmlDeviceGetMaxPcieLinkGeneration
@ stub nvmlDeviceGetMaxPcieLinkWidth
@ stub nvmlDeviceGetMemoryAffinity
@ stub nvmlDeviceGetMemoryErrorCounter
@ stdcall nvmlDeviceGetMemoryInfo(ptr ptr)
@ stub nvmlDeviceGetMigDeviceHandleByIndex
@ stub nvmlDeviceGetMigMode
@ stub nvmlDeviceGetMinorNumber
@ stub nvmlDeviceGetMultiGpuBoard
@ stdcall nvmlDeviceGetName(ptr str long)
@ stub nvmlDeviceGetNvLinkCapability
@ stub nvmlDeviceGetNvLinkErrorCounter
@ stub nvmlDeviceGetNvLinkRemotePciInfo
@ stub nvmlDeviceGetNvLinkRemotePciInfo_v2
@ stub nvmlDeviceGetNvLinkState
@ stub nvmlDeviceGetNvLinkUtilizationControl
@ stub nvmlDeviceGetNvLinkUtilizationCounter
@ stub nvmlDeviceGetNvLinkVersion
@ stub nvmlDeviceGetP2PStatus
@ stdcall nvmlDeviceGetPciInfo(ptr ptr)
@ stdcall nvmlDeviceGetPciInfo_v2(ptr ptr)
@ stdcall nvmlDeviceGetPciInfo_v3(ptr ptr)
@ stub nvmlDeviceGetPcieReplayCounter
@ stub nvmlDeviceGetPcieThroughput
@ stdcall nvmlDeviceGetPerformanceState(ptr ptr)
@ stub nvmlDeviceGetPersistenceMode
@ stub nvmlDeviceGetPgpuMetadataString
@ stub nvmlDeviceGetPowerManagementDefaultLimit
@ stub nvmlDeviceGetPowerManagementLimit
@ stub nvmlDeviceGetPowerManagementLimitConstraints
@ stub nvmlDeviceGetPowerManagementMode
@ stub nvmlDeviceGetPowerState
@ stdcall nvmlDeviceGetPowerUsage(ptr ptr)
@ stub nvmlDeviceGetProcessUtilization
@ stub nvmlDeviceGetRemappedRows
@ stub nvmlDeviceGetRetiredPages
@ stub nvmlDeviceGetRetiredPagesPendingStatus
@ stub nvmlDeviceGetRetiredPages_v2
@ stub nvmlDeviceGetRowRemapperHistogram
@ stub nvmlDeviceGetSamples
@ stdcall nvmlDeviceGetSerial(ptr str long)
@ stub nvmlDeviceGetSupportedClocksThrottleReasons
@ stub nvmlDeviceGetSupportedEventTypes
@ stub nvmlDeviceGetSupportedGraphicsClocks
@ stub nvmlDeviceGetSupportedMemoryClocks
@ stub nvmlDeviceGetSupportedVgpus
@ stdcall nvmlDeviceGetTemperature(ptr long ptr)
@ stdcall nvmlDeviceGetTemperatureThreshold(ptr long ptr)
@ stub nvmlDeviceGetTopologyCommonAncestor
@ stub nvmlDeviceGetTopologyNearestGpus
@ stub nvmlDeviceGetTotalEccErrors
@ stub nvmlDeviceGetTotalEnergyConsumption
@ stdcall nvmlDeviceGetUUID(ptr str long)
@ stdcall nvmlDeviceGetUtilizationRates(ptr ptr)
@ stdcall nvmlDeviceGetVbiosVersion(ptr str long)
@ stub nvmlDeviceGetVgpuMetadata
@ stub nvmlDeviceGetVgpuProcessUtilization
@ stub nvmlDeviceGetVgpuUtilization
@ stub nvmlDeviceGetViolationStatus
@ stub nvmlDeviceGetVirtualizationMode
@ stub nvmlDeviceIsMigDeviceHandle
@ stub nvmlDeviceModifyDrainState
@ stub nvmlDeviceOnSameBoard
@ stub nvmlDeviceQueryDrainState
@ stub nvmlDeviceRegisterEvents
@ stub nvmlDeviceRemoveGpu
@ stub nvmlDeviceRemoveGpu_v2
@ stub nvmlDeviceResetApplicationsClocks
@ stub nvmlDeviceResetGpuLockedClocks
@ stub nvmlDeviceResetNvLinkErrorCounters
@ stub nvmlDeviceResetNvLinkUtilizationCounter
@ stub nvmlDeviceSetAPIRestriction
@ stub nvmlDeviceSetAccountingMode
@ stub nvmlDeviceSetApplicationsClocks
@ stub nvmlDeviceSetAutoBoostedClocksEnabled
@ stdcall nvmlDeviceSetComputeMode(ptr long)
@ stub nvmlDeviceSetCpuAffinity
@ stub nvmlDeviceSetDefaultAutoBoostedClocksEnabled
@ stub nvmlDeviceSetDriverModel
@ stub nvmlDeviceSetEccMode
@ stub nvmlDeviceSetGpuLockedClocks
@ stub nvmlDeviceSetGpuOperationMode
@ stub nvmlDeviceSetMigMode
@ stub nvmlDeviceSetNvLinkUtilizationControl
@ stub nvmlDeviceSetPersistenceMode
@ stub nvmlDeviceSetPowerManagementLimit
@ stub nvmlDeviceSetTemperatureThreshold
@ stub nvmlDeviceSetVirtualizationMode
@ stub nvmlDeviceValidateInforom
@ stdcall nvmlErrorString(long)
@ stub nvmlEventSetCreate
@ stub nvmlEventSetFree
@ stub nvmlEventSetWait
@ stub nvmlEventSetWait_v2
@ stub nvmlGetBlacklistDeviceCount
@ stub nvmlGetBlacklistDeviceInfoByIndex
@ stub nvmlGetVgpuCompatibility
@ stub nvmlGetVgpuVersion
@ stub nvmlGpuInstanceCreateComputeInstance
@ stub nvmlGpuInstanceDestroy
@ stub nvmlGpuInstanceGetComputeInstanceById
@ stub nvmlGpuInstanceGetComputeInstanceProfileInfo
@ stub nvmlGpuInstanceGetComputeInstanceRemainingCapacity
@ stub nvmlGpuInstanceGetComputeInstances
@ stub nvmlGpuInstanceGetInfo
@ stub nvmlInit
@ stdcall nvmlInitWithFlags(long)
@ stdcall nvmlInit_v2()
@ stub nvmlInternalGetExportTable
@ stub nvmlSetVgpuVersion
@ stdcall nvmlShutdown()
@ stdcall nvmlSystemGetCudaDriverVersion(ptr)
@ stdcall nvmlSystemGetCudaDriverVersion_v2(ptr)
@ stdcall nvmlSystemGetDriverVersion(str long)
@ stub nvmlSystemGetHicVersion
@ stdcall nvmlSystemGetNVMLVersion(str long)
@ stub nvmlSystemGetProcessName
@ stub nvmlSystemGetTopologyGpuSet
@ stub nvmlUnitGetCount
@ stub nvmlUnitGetDevices
@ stub nvmlUnitGetFanSpeedInfo
@ stub nvmlUnitGetHandleByIndex
@ stub nvmlUnitGetLedState
@ stub nvmlUnitGetPsuInfo
@ stub nvmlUnitGetTemperature
@ stub nvmlUnitGetUnitInfo
@ stub nvmlUnitSetLedState
@ stub nvmlVgpuInstanceClearAccountingPids
@ stub nvmlVgpuInstanceGetAccountingMode
@ stub nvmlVgpuInstanceGetAccountingPids
@ stub nvmlVgpuInstanceGetAccountingStats
@ stub nvmlVgpuInstanceGetEccMode
@ stub nvmlVgpuInstanceGetEncoderCapacity
@ stub nvmlVgpuInstanceGetEncoderSessions
@ stub nvmlVgpuInstanceGetEncoderStats
@ stub nvmlVgpuInstanceGetFBCSessions
@ stub nvmlVgpuInstanceGetFBCStats
@ stub nvmlVgpuInstanceGetFbUsage
@ stub nvmlVgpuInstanceGetFrameRateLimit
@ stub nvmlVgpuInstanceGetGpuInstanceId
@ stub nvmlVgpuInstanceGetLicenseStatus
@ stub nvmlVgpuInstanceGetMdevUUID
@ stub nvmlVgpuInstanceGetMetadata
@ stub nvmlVgpuInstanceGetType
@ stub nvmlVgpuInstanceGetUUID
@ stub nvmlVgpuInstanceGetVmDriverVersion
@ stub nvmlVgpuInstanceGetVmID
@ stub nvmlVgpuInstanceSetEncoderCapacity
@ stub nvmlVgpuTypeGetClass
@ stub nvmlVgpuTypeGetDeviceID
@ stub nvmlVgpuTypeGetFrameRateLimit
@ stub nvmlVgpuTypeGetFramebufferSize
@ stub nvmlVgpuTypeGetGpuInstanceProfileId
@ stub nvmlVgpuTypeGetLicense
@ stub nvmlVgpuTypeGetMaxInstances
@ stub nvmlVgpuTypeGetMaxInstancesPerVm
@ stub nvmlVgpuTypeGetName
@ stub nvmlVgpuTypeGetNumDisplayHeads
@ stub nvmlVgpuTypeGetResolution