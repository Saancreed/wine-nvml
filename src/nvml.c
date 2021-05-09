/*
 * Copyright (C) 2021 Krzysztof Bogacki
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA
 *
 */

#include "config.h"
#include "wine/port.h"

#include <stdarg.h>

#include "windef.h"
#include "winbase.h"
#include "wine/debug.h"

WINE_DEFAULT_DEBUG_CHANNEL(nvml);

#define _WINDOWS
#define NVML_LIB_EXPORT
#define NVML_NO_UNVERSIONED_FUNC_DEFS

#pragma push_macro("__declspec")
#undef __declspec
#define __declspec(x) __cdecl
#include "nvml.h"
#pragma pop_macro("__declspec")

static void *libnvidia_ml_handle = NULL;

static const char* (*pnvmlErrorString)(nvmlReturn_t result) = NULL;
static nvmlReturn_t (*pnvmlInitWithFlags)(unsigned int flags) = NULL;
static nvmlReturn_t (*pnvmlInit_v2)(void) = NULL;
static nvmlReturn_t (*pnvmlShutdown)(void) = NULL;
static nvmlReturn_t (*pnvmlSystemGetCudaDriverVersion)(int *cudaDriverVersion) = NULL;
static nvmlReturn_t (*pnvmlSystemGetCudaDriverVersion_v2)(int *cudaDriverVersion) = NULL;
static nvmlReturn_t (*pnvmlSystemGetDriverVersion)(char *version, unsigned int length) = NULL;
static nvmlReturn_t (*pnvmlSystemGetNVMLVersion)(char *version, unsigned int length) = NULL;

static nvmlReturn_t (*pnvmlDeviceGetClock)(nvmlDevice_t device, nvmlClockType_t clockType, nvmlClockId_t clockId, unsigned int *clockMHz) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetComputeMode)(nvmlDevice_t device, nvmlComputeMode_t *mode) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetCount_v2)(unsigned int *deviceCount) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetCurrPcieLinkWidth)(nvmlDevice_t device, unsigned int *currLinkWidth) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetCurrentClocksThrottleReasons)(nvmlDevice_t device, unsigned long long *clocksThrottleReasons) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetDecoderUtilization)(nvmlDevice_t device, unsigned int *utilization, unsigned int *samplingPeriodUs) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetEncoderUtilization)(nvmlDevice_t device, unsigned int *utilization, unsigned int *samplingPeriodUs) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetEnforcedPowerLimit)(nvmlDevice_t device, unsigned int *limit) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetFanSpeed_v2)(nvmlDevice_t device, unsigned int fan, unsigned int *speed) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetHandleByIndex)(unsigned int index, nvmlDevice_t *device) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetHandleByIndex_v2)(unsigned int index, nvmlDevice_t *device) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetHandleByPciBusId)(const char *pciBusId, nvmlDevice_t *device) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetHandleByPciBusId_v2)(const char *pciBusId, nvmlDevice_t *device) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetHandleBySerial)(const char *serial, nvmlDevice_t *device) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetHandleByUUID)(const char *uuid, nvmlDevice_t *device) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetIndex)(nvmlDevice_t device, unsigned int *index) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetMemoryInfo)(nvmlDevice_t device, nvmlMemory_t *memory) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetName)(nvmlDevice_t device, char *name, unsigned int length) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetPciInfo)(nvmlDevice_t device, nvmlPciInfo_t *pci) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetPciInfo_v2)(nvmlDevice_t device, nvmlPciInfo_t *pci) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetPciInfo_v3)(nvmlDevice_t device, nvmlPciInfo_t *pci) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetPerformanceState)(nvmlDevice_t device, nvmlPstates_t *pState) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetPowerUsage)(nvmlDevice_t device, unsigned int *power) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetSerial)(nvmlDevice_t device, char *serial, unsigned int length) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetTemperature)(nvmlDevice_t device, nvmlTemperatureSensors_t sensorType, unsigned int *temp) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetTemperatureThreshold)(nvmlDevice_t device, nvmlTemperatureThresholds_t thresholdType, unsigned int *temp) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetUUID)(nvmlDevice_t device, char *uuid, unsigned int length) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetUtilizationRates)(nvmlDevice_t device, nvmlUtilization_t *utilization) = NULL;
static nvmlReturn_t (*pnvmlDeviceGetVbiosVersion)(nvmlDevice_t device, char *version, unsigned int length) = NULL;
static nvmlReturn_t (*pnvmlDeviceSetComputeMode)(nvmlDevice_t device, nvmlComputeMode_t mode) = NULL;

const char* __cdecl nvmlErrorString(nvmlReturn_t result)
{
    TRACE("(%u)\n", result);
    return pnvmlErrorString(result);
}

nvmlReturn_t __cdecl nvmlInitWithFlags(unsigned int flags)
{
    TRACE("(%u)\n", flags);
    return pnvmlInitWithFlags(flags);
}

nvmlReturn_t __cdecl nvmlInit_v2(void)
{
    TRACE("()\n");
    return pnvmlInit_v2();
}

nvmlReturn_t __cdecl nvmlInternalGetExportTable(size_t *exportTable, GUID *guid)
{
    FIXME("(%p, %s): stub\n", exportTable, debugstr_guid(guid));
    return NVML_ERROR_INVALID_ARGUMENT;
}

nvmlReturn_t __cdecl nvmlShutdown(void)
{
    TRACE("()\n");
    return pnvmlShutdown();
}

nvmlReturn_t __cdecl nvmlSystemGetCudaDriverVersion(int *cudaDriverVersion)
{
    TRACE("(%p)\n", cudaDriverVersion);
    return pnvmlSystemGetCudaDriverVersion(cudaDriverVersion);
}

nvmlReturn_t __cdecl nvmlSystemGetCudaDriverVersion_v2(int *cudaDriverVersion)
{
    TRACE("(%p)\n", cudaDriverVersion);
    return pnvmlSystemGetCudaDriverVersion_v2(cudaDriverVersion);
}

nvmlReturn_t __cdecl nvmlSystemGetDriverVersion(char *version, unsigned int length)
{
    TRACE("(%p, %u)\n", version, length);
    return pnvmlSystemGetDriverVersion(version, length);
}

nvmlReturn_t __cdecl nvmlSystemGetNVMLVersion(char *version, unsigned int length)
{
    TRACE("(%p, %u)\n", version, length);
    return pnvmlSystemGetNVMLVersion(version, length);
}

nvmlReturn_t __cdecl nvmlDeviceGetClock(nvmlDevice_t device, nvmlClockType_t clockType, nvmlClockId_t clockId, unsigned int *clockMHz)
{
    TRACE("(%p, %u, %u, %p)\n", device, clockType, clockId, clockMHz);
    return pnvmlDeviceGetClock
        ? pnvmlDeviceGetClock(device, clockType, clockId, clockMHz)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetComputeMode(nvmlDevice_t device, nvmlComputeMode_t *mode)
{
    TRACE("(%p, %p)\n", device, mode);
    return pnvmlDeviceGetComputeMode
        ? pnvmlDeviceGetComputeMode(device, mode)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetCount_v2(unsigned int *deviceCount)
{
    TRACE("(%p)\n", deviceCount);
    return pnvmlDeviceGetCount_v2
        ? pnvmlDeviceGetCount_v2(deviceCount)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetCurrPcieLinkWidth(nvmlDevice_t device, unsigned int *currLinkWidth)
{
    TRACE("(%p, %p)\n", device, currLinkWidth);
    return pnvmlDeviceGetCurrPcieLinkWidth
        ? pnvmlDeviceGetCurrPcieLinkWidth(device, currLinkWidth)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetCurrentClocksThrottleReasons(nvmlDevice_t device, unsigned long long *clocksThrottleReasons)
{
    TRACE("(%p, %p)\n", device, clocksThrottleReasons);
    return pnvmlDeviceGetCurrentClocksThrottleReasons
        ? pnvmlDeviceGetCurrentClocksThrottleReasons(device, clocksThrottleReasons)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetDecoderUtilization(nvmlDevice_t device, unsigned int *utilization, unsigned int *samplingPeriodUs)
{
    TRACE("(%p, %p, %p)\n", device, utilization, samplingPeriodUs);
    return pnvmlDeviceGetDecoderUtilization
        ? pnvmlDeviceGetDecoderUtilization(device, utilization, samplingPeriodUs)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetEncoderUtilization(nvmlDevice_t device, unsigned int *utilization, unsigned int *samplingPeriodUs)
{
    TRACE("(%p, %p, %p)\n", device, utilization, samplingPeriodUs);
    return pnvmlDeviceGetEncoderUtilization
        ? pnvmlDeviceGetEncoderUtilization(device, utilization, samplingPeriodUs)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetEnforcedPowerLimit(nvmlDevice_t device, unsigned int *limit)
{
    TRACE("(%p, %p)\n", device, limit);
    return pnvmlDeviceGetEnforcedPowerLimit
        ? pnvmlDeviceGetEnforcedPowerLimit(device, limit)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetFanSpeed_v2(nvmlDevice_t device, unsigned int fan, unsigned int *speed)
{
    TRACE("(%p, %u, %p)\n", device, fan, speed);
    return pnvmlDeviceGetFanSpeed_v2
        ? pnvmlDeviceGetFanSpeed_v2(device, fan, speed)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetHandleByIndex(unsigned int index, nvmlDevice_t *device)
{
    TRACE("(%u, %p)\n", index, device);
    return pnvmlDeviceGetHandleByIndex
        ? pnvmlDeviceGetHandleByIndex(index, device)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetHandleByIndex_v2(unsigned int index, nvmlDevice_t *device)
{
    TRACE("(%u, %p)\n", index, device);
    return pnvmlDeviceGetHandleByIndex_v2
        ? pnvmlDeviceGetHandleByIndex_v2(index, device)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetHandleByPciBusId(const char *pciBusId, nvmlDevice_t *device)
{
    TRACE("(%s, %p)\n", pciBusId, device);
    return pnvmlDeviceGetHandleByPciBusId
        ? pnvmlDeviceGetHandleByPciBusId(pciBusId, device)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetHandleByPciBusId_v2(const char *pciBusId, nvmlDevice_t *device)
{
    TRACE("(%s, %p)\n", pciBusId, device);
    return pnvmlDeviceGetHandleByPciBusId_v2
        ? pnvmlDeviceGetHandleByPciBusId_v2(pciBusId, device)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetHandleBySerial(const char *serial, nvmlDevice_t *device)
{
    TRACE("(%s, %p)\n", serial, device);
    return pnvmlDeviceGetHandleBySerial
        ? pnvmlDeviceGetHandleBySerial(serial, device)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetHandleByUUID(const char *uuid, nvmlDevice_t *device)
{
    TRACE("(%s, %p)\n", uuid, device);
    return pnvmlDeviceGetHandleByUUID
        ? pnvmlDeviceGetHandleByUUID(uuid, device)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetIndex(nvmlDevice_t device, unsigned int *index)
{
    TRACE("(%p, %p)\n", device, index);
    return pnvmlDeviceGetIndex
        ? pnvmlDeviceGetIndex(device, index)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetMemoryInfo(nvmlDevice_t device, nvmlMemory_t *memory)
{
    TRACE("(%p, %p)\n", device, memory);
    return pnvmlDeviceGetMemoryInfo
        ? pnvmlDeviceGetMemoryInfo(device, memory)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetName(nvmlDevice_t device, char *name, unsigned int length)
{
    TRACE("(%p, %p, %u)\n", device, name, length);
    return pnvmlDeviceGetName
        ? pnvmlDeviceGetName(device, name, length)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetPciInfo(nvmlDevice_t device, nvmlPciInfo_t *pci)
{
    TRACE("(%p, %p)\n", device, pci);
    return pnvmlDeviceGetPciInfo
        ? pnvmlDeviceGetPciInfo(device, pci)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetPciInfo_v2(nvmlDevice_t device, nvmlPciInfo_t *pci)
{
    TRACE("(%p, %p)\n", device, pci);
    return pnvmlDeviceGetPciInfo_v2
        ? pnvmlDeviceGetPciInfo_v2(device, pci)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetPciInfo_v3(nvmlDevice_t device, nvmlPciInfo_t *pci)
{
    TRACE("(%p, %p)\n", device, pci);
    return pnvmlDeviceGetPciInfo_v3
        ? pnvmlDeviceGetPciInfo_v3(device, pci)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetPerformanceState(nvmlDevice_t device, nvmlPstates_t *pState)
{
    TRACE("(%p, %p)\n", device, pState);
    return pnvmlDeviceGetPerformanceState
        ? pnvmlDeviceGetPerformanceState(device, pState)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetPowerUsage(nvmlDevice_t device, unsigned int *power)
{
    TRACE("(%p, %p)\n", device, power);
    return pnvmlDeviceGetPowerUsage
        ? pnvmlDeviceGetPowerUsage(device, power)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetSerial(nvmlDevice_t device, char *serial, unsigned int length)
{
    TRACE("(%p, %p, %u)\n", device, serial, length);
    return pnvmlDeviceGetSerial
        ? pnvmlDeviceGetSerial(device, serial, length)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetTemperature(nvmlDevice_t device, nvmlTemperatureSensors_t sensorType, unsigned int *temp)
{
    TRACE("(%p, %u, %p)\n", device, sensorType, temp);
    return pnvmlDeviceGetTemperature
        ? pnvmlDeviceGetTemperature(device, sensorType, temp)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetTemperatureThreshold(nvmlDevice_t device, nvmlTemperatureThresholds_t thresholdType, unsigned int *temp)
{
    TRACE("(%p, %u, %p)\n", device, thresholdType, temp);
    return pnvmlDeviceGetTemperatureThreshold
        ? pnvmlDeviceGetTemperatureThreshold(device, thresholdType, temp)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetUUID(nvmlDevice_t device, char *uuid, unsigned int length)
{
    TRACE("(%p, %p, %u)\n", device, uuid, length);
    return pnvmlDeviceGetUUID
        ? pnvmlDeviceGetUUID(device, uuid, length)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetUtilizationRates(nvmlDevice_t device, nvmlUtilization_t *utilization)
{
    TRACE("(%p, %p)\n", device, utilization);
    return pnvmlDeviceGetUtilizationRates
        ? pnvmlDeviceGetUtilizationRates(device, utilization)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceGetVbiosVersion(nvmlDevice_t device, char *version, unsigned int length)
{
    TRACE("(%p, %p, %u)\n", device, version, length);
    return pnvmlDeviceGetVbiosVersion
        ? pnvmlDeviceGetVbiosVersion(device, version, length)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

nvmlReturn_t __cdecl nvmlDeviceSetComputeMode(nvmlDevice_t device, nvmlComputeMode_t mode)
{
    TRACE("(%p, %u)\n", device, mode);
    return pnvmlDeviceSetComputeMode
        ? pnvmlDeviceSetComputeMode(device, mode)
        : NVML_ERROR_FUNCTION_NOT_FOUND;
}

static BOOL load_nvml(void)
{
    if (!(libnvidia_ml_handle = dlopen("libnvidia-ml.so", RTLD_NOW)))
    {
        ERR("Wine cannot find the libnvidia-ml.so library, NVIDIA Management Library support disabled.\n");
        return FALSE;
    }

    #define LOAD_FUNCPTR(f) if (!(*(void **)(&p##f) = dlsym(libnvidia_ml_handle, #f))) { ERR("Can't find symbol %s.\n", #f); goto fail; }

    LOAD_FUNCPTR(nvmlErrorString);
    LOAD_FUNCPTR(nvmlInitWithFlags);
    LOAD_FUNCPTR(nvmlInit_v2);
    LOAD_FUNCPTR(nvmlShutdown);
    LOAD_FUNCPTR(nvmlSystemGetCudaDriverVersion);
    LOAD_FUNCPTR(nvmlSystemGetCudaDriverVersion_v2);
    LOAD_FUNCPTR(nvmlSystemGetDriverVersion);
    LOAD_FUNCPTR(nvmlSystemGetNVMLVersion);

    #undef LOAD_FUNCPTR

    #define TRY_LOAD_FUNCPTR(f) if (!(*(void **)(&p##f) = dlsym(libnvidia_ml_handle, #f))) { WARN("Can't find symbol %s.\n", #f); }

    TRY_LOAD_FUNCPTR(nvmlDeviceGetClock);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetComputeMode);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetCount_v2);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetCurrPcieLinkWidth);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetCurrentClocksThrottleReasons);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetDecoderUtilization);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetEncoderUtilization);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetEnforcedPowerLimit);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetFanSpeed_v2);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetHandleByIndex);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetHandleByIndex_v2);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetHandleByPciBusId);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetHandleByPciBusId_v2);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetHandleBySerial);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetHandleByUUID);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetIndex);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetMemoryInfo);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetName);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetPciInfo);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetPciInfo_v2);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetPciInfo_v3);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetPerformanceState);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetPowerUsage);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetSerial);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetTemperature);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetTemperatureThreshold);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetUUID);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetUtilizationRates);
    TRY_LOAD_FUNCPTR(nvmlDeviceGetVbiosVersion);
    TRY_LOAD_FUNCPTR(nvmlDeviceSetComputeMode);

    #undef TRY_LOAD_FUNCPTR

    return TRUE;

fail:
    dlclose(libnvidia_ml_handle);
    return FALSE;
}

BOOL WINAPI DllMain(HINSTANCE instance, DWORD reason, LPVOID reserved)
{
    TRACE("(%p, %u, %p)\n", instance, reason, reserved);

    switch (reason)
    {
        case DLL_PROCESS_ATTACH:
            DisableThreadLibraryCalls(instance);
            if (!load_nvml()) return FALSE;
            break;
        case DLL_PROCESS_DETACH:
            if (reserved) break;
            if (libnvidia_ml_handle) dlclose(libnvidia_ml_handle);
            break;
    }

    return TRUE;
}
