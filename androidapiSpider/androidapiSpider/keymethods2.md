getCarrierFrequencyHz:  
Gets the carrier frequency of the signal tracked. For example it can be the GPS central frequency for L1 = 1575.45 MHz, or L2 = 1227.60 MHz, L5 = 1176.45 MHz, varying GLO channels, etc. If the field is not set, it is the primary common use central frequency, e.g. L1 = 1575.45 MHz for GPS. For an L1, L5 receiver tracking a satellite on L1 and L5 at the same time, two measurements will be reported for this same satellite, in one all the values related to L1 will be filled, and in the other all of the values related to L5 will be filled. The value is only available if hasCarrierFrequencyHz(int) is true.

increment:  
Increment a value block, storing the result in the temporary block on the tag. This is an I/O operation and will block until complete. It must not be called from the main application thread. A blocked call will be canceled with IOException if close() is called from another thread. Requires the NFC permission.

connect:  
Enable I/O operations to the tag from this TagTechnology object. May cause RF activity and may block. Must not be called from the main application thread. A blocked call will be canceled with IOException by calling close() from another thread. Only one TagTechnology object can be connected to a Tag at a time. Applications must call close() when I/O operations are complete. Requires the NFC permission.

unlock:  
Unlocks the camera to allow another process to access it. Normally, the camera is locked to the process with an active Camera object until release() is called.  To allow rapid handoff between processes, you can call this method to release the camera temporarily for another process to use; once the other process is done you can call reconnect() to reclaim the camera. This must be done before calling setCamera(Camera). This cannot be called after recording starts. If you are not recording video, you probably do not need this method.

setUnderlyingNetworks:  
Sets the underlying networks used by the VPN for its upstream connections. Used by the system to know the actual networks that carry traffic for apps affected by this VPN in order to present this information to the user (e.g., via status bar icons). This method only needs to be called if the VPN has explicitly bound its underlying communications channels ！ such as the socket(s) passed to protect(int) ！ to a Network using APIs such as bindSocket(Socket) or bindSocket(DatagramSocket). The VPN should call this method every time the set of Networks it is using changes. networks is one of the following: a non-empty array: an array of one or more Networks, in decreasing preference order. For example, if this VPN uses both wifi and mobile (cellular) networks to carry app traffic, but prefers or uses wifi more than mobile, wifi should appear first in the array. an empty array: a zero-element array, meaning that the VPN has no underlying network connection, and thus, app traffic will not be sent or received. null: (default) signifies that the VPN uses whatever is the system's default network. I.e., it doesn't use the bindSocket or bindDatagramSocket APIs mentioned above to send traffic over specific channels.  This call will succeed only if the VPN is currently established. For setting this value when the VPN has not yet been established, see setUnderlyingNetworks(Network[]).

setLookasideConfig:  
Configures lookaside memory allocator This method should be called from the constructor of the subclass, before opening the database, since lookaside memory configuration can only be changed when no connection is using it SQLite default settings will be used, if this method isn't called. Use setLookasideConfig(0,0) to disable lookaside Note: Provided slotSize/slotCount configuration is just a recommendation. The system may choose different values depending on a device, e.g. lookaside allocations can be disabled on low-RAM devices

sendTextMessageWithoutPersisting:  
Send a text based SMS without writing it into the SMS Provider. The message will be sent directly over the network and will not be visible in SMS applications. Intended for internal carrier use only.  Requires Permission: Both SEND_SMS and MODIFY_PHONE_STATE, or that the calling app has carrier privileges (see hasCarrierPrivileges()), or that the calling app is the default IMS app (see KEY_CONFIG_IMS_PACKAGE_OVERRIDE_STRING).   See also: sendTextMessage(String, String, String, PendingIntent, PendingIntent)

isWritable:  
Determine if the tag is writable. NFC Forum tags can be in read-only or read-write states. Does not cause any RF activity and does not block. Requires NFC permission.

setPreferredPhy:  
Set the preferred connection PHY for this app. Please note that this is just a recommendation, whether the PHY change will happen depends on other applications peferences, local and remote controller capabilities. Controller can override these settings. onPhyUpdate(BluetoothDevice, int, int, int) will be triggered as a result of this call, even if no PHY change happens. It is also triggered when remote device updates the PHY.

setTimeout:  
Set the transceive(byte[]) timeout in milliseconds. The timeout only applies to transceive(byte[]) on this object, and is reset to a default value when close() is called. Setting a longer timeout may be useful when performing transactions that require a long processing time on the tag such as key generation. Requires the NFC permission.

isDiscovering:  
Return true if the local Bluetooth adapter is currently in the device discovery process. Device discovery is a heavyweight procedure. New connections to remote Bluetooth devices should not be attempted while discovery is in progress, and existing connections will experience limited bandwidth and high latency. Use cancelDiscovery() to cancel an ongoing discovery. Applications can also register for ACTION_DISCOVERY_STARTED or ACTION_DISCOVERY_FINISHED to be notified when discovery starts or completes. If Bluetooth state is not STATE_ON, this API will return false. After turning on Bluetooth, wait for ACTION_STATE_CHANGED with STATE_ON to get the updated value. Requires the BLUETOOTH permission.

onRestoreFile:  
Handle the data delivered via the given file descriptor during a full restore operation.  The agent is given the path to the file's original location as well as its size and metadata. The file descriptor can only be read for size bytes; attempting to read more data has undefined behavior. The default implementation creates the destination file/directory and populates it with the data from the file descriptor, then sets the file's access mode and modification time to match the restore arguments.

setBearingAccuracyDegrees:  
Set the estimated bearing accuracy of this location, degrees. See getBearingAccuracyDegrees() for the definition of bearing accuracy. Following this call hasBearingAccuracy() will return true.

setOnShareTargetSelectedListener:  
Sets a listener to be notified when a share target has been selected. The listener can optionally decide to handle the selection and not rely on the default behavior which is to launch the activity. Note: If you choose the backing share history file     you will still be notified in this callback.

transceive:  
Send raw NFC-F commands to the tag and receive the response. Applications must not prefix the SoD (preamble and sync code) and/or append the EoD (CRC) to the payload, it will be automatically calculated. A typical NFC-F frame for this method looks like: LENGTH (1 byte) --- CMD (1 byte) -- IDm (8 bytes) -- PARAMS (LENGTH - 10 bytes)  Use getMaxTransceiveLength() to retrieve the maximum amount of bytes that can be sent with transceive(byte[]). This is an I/O operation and will block until complete. It must not be called from the main application thread. A blocked call will be canceled with IOException if close() is called from another thread. Requires the NFC permission.

setStorageDefault:  
Sets the storage location used internally by this class to be the default provided by the hosting Context.

takePicture:  
Triggers an asynchronous image capture. The camera service will initiate a series of callbacks to the application as the image capture progresses. The shutter callback occurs after the image is captured. This can be used to trigger a sound to let the user know that image has been captured. The raw callback occurs when the raw image data is available (NOTE: the data will be null if there is no raw image callback buffer available or the raw image callback buffer is not large enough to hold the raw image). The postview callback occurs when a scaled, fully processed postview image is available (NOTE: not all hardware supports this). The jpeg callback occurs when the compressed image is available. If the application does not need a particular callback, a null can be passed instead of a callback method. This method is only valid when preview is active (after startPreview()).  Preview will be stopped after the image is taken; callers must call startPreview() again if they want to re-start preview or take more pictures. This should not be called between start() and stop(). After calling this method, you must not call startPreview() or take another picture until the JPEG callback has returned.

getTimeout:  
Get the current transceive(byte[]) timeout in milliseconds. Requires the NFC permission.

showAtLocation:  
Display the content view in a popup window at the specified location. If the popup window cannot fit on screen, it will be clipped. See WindowManager.LayoutParams for more information on how gravity and the x and y parameters are related. Specifying a gravity of NO_GRAVITY is similar to specifying Gravity.LEFT | Gravity.TOP.

SparseArray:  
Creates a new SparseArray containing no mappings that will not require any additional memory allocation to store the specified number of mappings.  If you supply an initial capacity of 0, the sparse array will be initialized with a light-weight representation not requiring any additional array allocations.

startRanging:  
Initiate a request to range to a set of devices specified in the RangingRequest. Results will be returned in the RangingResultCallback set of callbacks. Requires the ACCESS_FINE_LOCATION, CHANGE_WIFI_STATE and ACCESS_WIFI_STATE permissions.

setPhone:  
Sets the phone number associated with this address.

makeReadOnly:  
Make a tag read-only. This sets the CC field to indicate the tag is read-only, and where possible permanently sets the lock bits to prevent any further modification of the memory. This is a one-way process and cannot be reverted! This is an I/O operation and will block until complete. It must not be called from the main application thread. A blocked call will be canceled with IOException if close() is called from another thread. Requires the NFC permission.

formatReadOnly:  
Formats a tag as NDEF, write a NdefMessage, and make read-only. This is a multi-step process, an IOException is thrown if any one step fails. The card is left in a read-only state if this method returns successfully. This is an I/O operation and will block until complete. It must not be called from the main application thread. A blocked call will be canceled with IOException if close() is called from another thread. Requires the NFC permission.

setVerticalAccuracy:  
Indicates the desired vertical accuracy (altitude). Accuracy may be ACCURACY_LOW, ACCURACY_MEDIUM, ACCURACY_HIGH or NO_REQUIREMENT. More accurate location may consume more power and may take longer.

setAutoFocusMoveCallback:  
Sets camera auto-focus move callback.

onSendMultipartTextSms:  
Override this method to intercept long SMSs sent from the device.

isStorageDeviceProtected:  
Indicates if the storage location used internally by this class is backed by device-protected storage.   See also: setStorageDefault()setStorageDeviceProtected()

getVerticalAccuracyMeters:  
Get the estimated vertical accuracy of this location, in meters. We define vertical accuracy at 68% confidence.  Specifically, as 1-side of the 2-sided range above and below the estimated altitude reported by getAltitude(), within which there is a 68% probability of finding the true altitude. In the case where the underlying distribution is assumed Gaussian normal, this would be considered 1 standard deviation. For example, if getAltitude() returns 150, and getVerticalAccuracyMeters() returns 20 then there is a 68% probability of the true altitude being between 130 and 170 meters. If this location does not have a vertical accuracy, then 0.0 is returned.

acquire:  
Locks the Wi-Fi radio on until release() is called. If this WifiLock is reference-counted, each call to acquire will increment the reference count, and the radio will remain locked as long as the reference count is above zero. If this WifiLock is not reference-counted, the first call to acquire will lock the radio, but subsequent calls will be ignored.  Only one call to release() will be required, regardless of the number of times that acquire is called.

setStorageDeviceProtected:  
Explicitly set the storage location used internally by this class to be device-protected storage. On devices with direct boot, data stored in this location is encrypted with a key tied to the physical device, and it can be accessed immediately after the device has booted successfully, both before and after the user has authenticated with their credentials (such as a lock pattern or PIN). Because device-protected data is available without user authentication, you should carefully limit the data you store using this Context. For example, storing sensitive authentication tokens or passwords in the device-protected area is strongly discouraged.  See also: createDeviceProtectedStorageContext()

onResume:  
Called after onRestoreInstanceState(Bundle), onRestart(), or onPause(), for your activity to start interacting with the user. This is a good place to begin animations, open exclusive-access devices (such as the camera), etc. Keep in mind that onResume is not the best indicator that your activity is visible to the user; a system window such as the keyguard may be in front.  Use onWindowFocusChanged(boolean) to know for certain that your activity is visible to the user (for example, to resume a game). Derived classes must call through to the super class's implementation of this method.  If they do not, an exception will be thrown.

registerGnssNavigationMessageCallback:  
Registers a GNSS Navigation Message callback. Requires the ACCESS_FINE_LOCATION permission.

VideoProfile.CameraCapabilities:  
Create a call camera capabilities instance.

SparseBooleanArray:  
Creates a new SparseBooleanArray containing no mappings that will not require any additional memory allocation to store the specified number of mappings.  If you supply an initial capacity of 0, the sparse array will be initialized with a light-weight representation not requiring any additional array allocations.

setParameters:  
Changes the settings for this Camera service.    See also: getParameters()

drag:  
Simulate touching a specific location and dragging to a new location.

setDisplayOrientation:  
Set the clockwise rotation of preview display in degrees. This affects the preview frames and the picture displayed after snapshot. This method is useful for portrait mode applications. Note that preview display of front-facing cameras is flipped horizontally before the rotation, that is, the image is reflected along the central vertical axis of the camera sensor. So the users can see themselves as looking into a mirror. This does not affect the order of byte array passed in onPreviewFrame(byte[], Camera), JPEG pictures, or recorded videos. This method is not allowed to be called during preview. If you want to make the camera image show in the same orientation as the display, you can use the following code. public static void setCameraDisplayOrientation(Activity activity,         int cameraId, android.hardware.Camera camera) {     android.hardware.Camera.CameraInfo info =             new android.hardware.Camera.CameraInfo();     android.hardware.Camera.getCameraInfo(cameraId, info);     int rotation = activity.getWindowManager().getDefaultDisplay()             .getRotation();     int degrees = 0;     switch (rotation) {         case Surface.ROTATION_0: degrees = 0; break;         case Surface.ROTATION_90: degrees = 90; break;         case Surface.ROTATION_180: degrees = 180; break;         case Surface.ROTATION_270: degrees = 270; break;     }     int result;     if (info.facing == Camera.CameraInfo.CAMERA_FACING_FRONT) {         result = (info.orientation + degrees) % 360;         result = (360 - result) % 360;  // compensate the mirror     } else {  // back-facing         result = (info.orientation - degrees + 360) % 360;     }     camera.setDisplayOrientation(result); }  Starting from API level 14, this method can be called when preview is active. Note: Before API level 24, the default value for orientation is 0. Starting in API level 24, the default orientation will be such that applications in forced-landscape mode will have correct preview orientation, which may be either a default of 0 or 180. Applications that operate in portrait mode or allow for changing orientation must still call this method after each orientation change to ensure correct preview display in all cases.    See also: setPreviewDisplay(SurfaceHolder)

registerAvailabilityCallback:  
Register a callback to be notified about camera device availability. Registering the same callback again will replace the handler with the new one provided.  The first time a callback is registered, it is immediately called with the availability status of all currently known camera devices.  onCameraUnavailable(String) will be called whenever a camera device is opened by any camera API client. As of API level 23, other camera API clients may still be able to open such a camera device, evicting the existing client if they have higher priority than the existing client of a camera device. See open() for more details.  Since this callback will be registered with the camera service, remember to unregister it once it is no longer needed; otherwise the callback will continue to receive events indefinitely and it may prevent other resources from being released. Specifically, the callbacks will be invoked independently of the general activity lifecycle and independently of the state of individual CameraManager instances.

compare:  
Compare phone numbers a and b, return true if they're identical enough for caller ID purposes.

assertRightAligned:  
Assert that two views are right aligned, that is that their right edges are on the same x location, with respect to the specified margin.

setTimeout:  
Set the timeout of transceive(byte[]) in milliseconds. The timeout only applies to ISO-DEP transceive(byte[]), and is reset to a default value when close() is called. Setting a longer timeout may be useful when performing transactions that require a long processing time on the tag such as key generation. Requires the NFC permission.

setLacAndCid:  
Set the location area code and the cell id.

getPrimaryHorizontal:  
Get the primary horizontal position for the specified text offset. This is the location where a new character would be inserted in the paragraph's primary direction.

abortCaptures:  
Discard all captures currently pending and in-progress as fast as possible. The camera device will discard all of its current work as fast as possible. Some in-flight captures may complete successfully and call onCaptureCompleted(CameraCaptureSession, CaptureRequest, TotalCaptureResult), while others will trigger their onCaptureFailed(CameraCaptureSession, CaptureRequest, CaptureFailure) callbacks. If a repeating request or a repeating burst is set, it will be cleared.  This method is the fastest way to switch the camera device to a new session with createCaptureSession(SessionConfiguration) or createReprocessableCaptureSession(InputConfiguration, List, CameraCaptureSession.StateCallback, Handler), at the cost of discarding in-progress work. It must be called before the new session is created. Once all pending requests are either completed or thrown away, the onReady(CameraCaptureSession) callback will be called, if the session has not been closed. Otherwise, the onClosed(CameraCaptureSession) callback will be fired when a new session is created by the camera device.  Cancelling will introduce at least a brief pause in the stream of data from the camera device, since once the camera device is emptied, the first new request has to make it through the entire camera pipeline before new output buffers are produced.  This means that using abortCaptures() to simply remove pending requests is not recommended; it's best used for quickly switching output configurations, or for cancelling long in-progress requests (such as a multi-second capture).   See also: setRepeatingRequest(CaptureRequest, CameraCaptureSession.CaptureCallback, Handler)setRepeatingBurst(List, CameraCaptureSession.CaptureCallback, Handler)createCaptureSession(SessionConfiguration)createReprocessableCaptureSession(InputConfiguration, List, CameraCaptureSession.StateCallback, Handler)

getLocationZ:  
Gets the z location of the camera.   See also: setLocation(float, float, float)

removeProximityAlert:  
Removes the proximity alert with the given PendingIntent. Before API version 17, this method could be used with ACCESS_FINE_LOCATION or ACCESS_COARSE_LOCATION. From API version 17 and onwards, this method requires ACCESS_FINE_LOCATION permission.

setHotspot:  
Specifies the hotspot's location within the drawable.

onChannelDisconnected:  
The channel to the framework has been disconnected. Application could try re-initializing using initialize(Context, Looper, WifiP2pManager.ChannelListener)

onLocationChanged:  
Called when the location has changed. There are no restrictions on the use of the supplied Location object.

bearingTo:  
Returns the approximate initial bearing in degrees East of true North when traveling along the shortest path between this location and the given location.  The shortest path is defined using the WGS84 ellipsoid.  Locations that are (nearly) antipodal may produce meaningless results.

setCallAudioState:  
Request to change the conference's audio routing to the specified state. The specified state can include audio routing (Bluetooth, Speaker, etc) and muting state.

protect:  
Convenience method to protect a Socket from VPN connections.    See also: protect(int)

forEach:  
Apply the filter to the input and save to the specified allocation.

onTorchModeChanged:  
A camera's torch mode has become enabled or disabled and can be changed via setTorchMode(String, boolean). The default implementation of this method does nothing.

onTorchModeUnavailable:  
A camera's torch mode has become unavailable to set via setTorchMode(String, boolean). If torch mode was previously turned on by calling setTorchMode(String, boolean), it will be turned off before onTorchModeUnavailable(String) is invoked. setTorchMode(String, boolean) will fail until the torch mode has entered a disabled or enabled state again.  The default implementation of this method does nothing.

setPublicId:  
Set the public identifier for this Source. The public identifier is always optional: if the application writer includes one, it will be provided as part of the location information.

isOutputSupportedFor:  
Determine whether or not output streams can be configured with a particular class as a consumer. The following list is generally usable for outputs: ImageReader - Recommended for image processing or streaming to external resources (such as a file or network) MediaRecorder - Recommended for recording video (simple to use) MediaCodec - Recommended for recording video (more complicated to use, with more flexibility) Allocation - Recommended for image processing with RenderScript SurfaceHolder - Recommended for low-power camera preview with SurfaceView SurfaceTexture - Recommended for OpenGL-accelerated preview processing or compositing with TextureView  Generally speaking this means that creating a Surface from that class may provide a producer endpoint that is suitable to be used with createCaptureSession(SessionConfiguration).  Since not all of the above classes support output of all format and size combinations, the particular combination should be queried with isOutputSupportedFor(Surface).     See also: createCaptureSession(SessionConfiguration)isOutputSupportedFor(Surface)

NdefMessage:  
Construct an NDEF Message by parsing raw bytes. Strict validation of the NDEF binary structure is performed: there must be at least one record, every record flag must be correct, and the total length of the message must match the length of the input data. This parser can handle chunked records, and converts them into logical NdefRecords within the message. Once the input data has been parsed to one or more logical records, basic validation of the tnf, type, id, and payload fields of each record is performed, as per the documentation on on NdefRecord(short, byte[], byte[], byte[]) If either strict validation of the binary format fails, or basic validation during record construction fails, a FormatException is thrown Deep inspection of the type, id and payload fields of each record is not performed, so it is possible to parse input that has a valid binary format and confirms to the basic validation requirements of NdefRecord(short, byte[], byte[], byte[]), but fails more strict requirements as specified by the NFC Forum. It is safe to re-use the data byte array after construction: this constructor will make an internal copy of all necessary fields.

forEach:  
Process an input buffer and place the histogram into the output allocation. The output allocation may be a narrower vector size than the input. In this case the vector size of the output is used to determine how many of the input channels are used in the computation. This is useful if you have an RGBA input buffer but only want the histogram for RGB. 1D and 2D input allocations are supported.

onCaptureStarted:  
This method is called when the camera device has started capturing the output image for the request, at the beginning of image exposure, or when the camera device has started processing an input image for a reprocess request. For a regular capture request, this callback is invoked right as the capture of a frame begins, so it is the most appropriate time for playing a shutter sound, or triggering UI indicators of capture.  The request that is being used for this capture is provided, along with the actual timestamp for the start of exposure. For a reprocess request, this timestamp will be the input image's start of exposure which matches the result timestamp field of the TotalCaptureResult that was used to create the reprocess request. This timestamp matches the timestamps that will be included in the result timestamp field, and in the buffers sent to each output Surface. These buffer timestamps are accessible through, for example, Image.getTimestamp() or getTimestamp(). The frame number included is equal to the frame number that will be included in getFrameNumber().  For the simplest way to play a shutter sound camera shutter or a video recording start/stop sound, see the MediaActionSound class.  The default implementation of this method does nothing.   See also: MediaActionSound

openCamera:  
Open a connection to a camera with the given ID. The behavior of this method matches that of openCamera(String, StateCallback, Handler), except that it uses Executor as an argument instead of Handler. Requires the CAMERA permission.    See also: getCameraIdList()setCameraDisabled(ComponentName, boolean)

fullBackupFile:  
Write an entire file as part of a full-backup operation.  The file's contents will be delivered to the backup destination along with the metadata necessary to place it with the proper location and permissions on the device where the data is restored. Attempting to back up files in directories that are ignored by the backup system will have no effect.  For example, if the app calls this method with a file inside the getNoBackupFilesDir() directory, it will be ignored. See onFullBackup(FullBackupDataOutput) for details on what directories are excluded from backups.

close:  
Close this capture session asynchronously. Closing a session frees up the target output Surfaces of the session for reuse with either a new session, or to other APIs that can draw to Surfaces.  Note that creating a new capture session with createCaptureSession(SessionConfiguration) will close any existing capture session automatically, and call the older session listener's onClosed(CameraCaptureSession) callback. Using createCaptureSession(SessionConfiguration) directly without closing is the recommended approach for quickly switching to a new session, since unchanged target outputs can be reused more efficiently.  Once a session is closed, all methods on it will throw an IllegalStateException, and any repeating requests or bursts are stopped (as if stopRepeating() was called). However, any in-progress capture requests submitted to the session will be completed as normal; once all captures have completed and the session has been torn down, onClosed(CameraCaptureSession) will be called.  Closing a session is idempotent; closing more than once has no effect.

reset:  
Clears the contents of the location.

SparseIntArray:  
Creates a new SparseIntArray containing no mappings that will not require any additional memory allocation to store the specified number of mappings.  If you supply an initial capacity of 0, the sparse array will be initialized with a light-weight representation not requiring any additional array allocations.

setPreviewSize:  
Sets the dimensions for preview pictures. If the preview has already started, applications should stop the preview first before changing preview size. The sides of width and height are based on camera orientation. That is, the preview size is the size before it is rotated by display orientation. So applications need to consider the display orientation while setting preview size. For example, suppose the camera supports both 480x320 and 320x480 preview sizes. The application wants a 3:2 preview ratio. If the display orientation is set to 0 or 180, preview size should be set to 480x320. If the display orientation is set to 90 or 270, preview size should be set to 320x480. The display orientation should also be considered while setting picture size and thumbnail size.   See also: setDisplayOrientation(int)getCameraInfo(int, CameraInfo)setPictureSize(int, int)setJpegThumbnailSize(int, int)

getMemoryInfo:  
Retrieves information about this processes memory usages. This information is broken down by how much is in use by dalvik, the native heap, and everything else. Note: this method directly retrieves memory information for the given process from low-level data available to it.  It may not be able to retrieve information about some protected allocations, such as graphics.  If you want to be sure you can see all information about allocations by the process, use getProcessMemoryInfo(int[]) instead.

restore:  
Copy from a value block to the temporary block. This is an I/O operation and will block until complete. It must not be called from the main application thread. A blocked call will be canceled with IOException if close() is called from another thread. Requires the NFC permission.

onStopJob:  
This method is called if the system has determined that you must stop execution of your job even before you've had a chance to call jobFinished(JobParameters, boolean). This will happen if the requirements specified at schedule time are no longer met. For example you may have requested WiFi with setRequiredNetworkType(int), yet while your job was executing the user toggled WiFi. Another example is if you had specified setRequiresDeviceIdle(boolean), and the phone left its idle maintenance window. You are solely responsible for the behavior of your application upon receipt of this message; your app will likely start to misbehave if you ignore it. Once this method returns, the system releases the wakelock that it is holding on behalf of the job.

setPreviewSurface:  
Sets the surface to be used for displaying a preview of what the user's camera is currently capturing for the RemoteConnection.VideoProvider.   See also: onSetPreviewSurface(Surface)

hasVerticalAccuracy:  
True if this location has a vertical accuracy.

onProvideShadowMetrics:  
Provides the metrics for the shadow image. These include the dimensions of the shadow image, and the point within that shadow that should be centered under the touch location while dragging. The default implementation sets the dimensions of the shadow to be the same as the dimensions of the View itself and centers the shadow under the touch point.

autoFocus:  
Starts camera auto-focus and registers a callback function to run when the camera is focused.  This method is only valid when preview is active (between startPreview() and before stopPreview()). Callers should check getFocusMode() to determine if this method should be called. If the camera does not support auto-focus, it is a no-op and onAutoFocus(boolean, Camera) callback will be called immediately. If your application should not be installed on devices without auto-focus, you must declare that your application uses auto-focus with the <uses-feature> manifest element.  If the current flash mode is not FLASH_MODE_OFF, flash may be fired during auto-focus, depending on the driver and camera hardware.  Auto-exposure lock getAutoExposureLock() and auto-white balance locks getAutoWhiteBalanceLock() do not change during and after autofocus. But auto-focus routine may stop auto-exposure and auto-white balance transiently during focusing. Stopping preview with stopPreview(), or triggering still image capture with takePicture(Camera.ShutterCallback, Camera.PictureCallback, Camera.PictureCallback), will not change the the focus position. Applications must call cancelAutoFocus to reset the focus.  If autofocus is successful, consider using MediaActionSound to properly play back an autofocus success sound to the user.    See also: cancelAutoFocus()setAutoExposureLock(boolean)setAutoWhiteBalanceLock(boolean)MediaActionSound

onCameraUnavailable:  
A previously-available camera has become unavailable for use. If an application had an active CameraDevice instance for the now-disconnected camera, that application will receive a disconnection error.  The default implementation of this method does nothing.

addBatch:  
Add a new movement to the batch of movements in this event.  The event's current location, position and size is updated to the new values. The current values in the event are added to a list of historical values. Only applies to ACTION_MOVE or ACTION_HOVER_MOVE events.

VideoProfile.CameraCapabilities:  
Create a call camera capabilities instance.

decrement:  
Decrement a value block, storing the result in the temporary block on the tag. This is an I/O operation and will block until complete. It must not be called from the main application thread. A blocked call will be canceled with IOException if close() is called from another thread. Requires the NFC permission.

getTimeout:  
Get the current transceive(byte[]) timeout in milliseconds. Requires the NFC permission.

CarrierMessagingService.SendMultipartSmsResult:  
Constructs a SendMultipartSmsResult with the send status and message references for the just-sent multipart SMS.

transceive:  
Send raw NFC-V commands to the tag and receive the response. Applications must not append the CRC to the payload, it will be automatically calculated. The application does provide FLAGS, CMD and PARAMETER bytes. Use getMaxTransceiveLength() to retrieve the maximum amount of bytes that can be sent with transceive(byte[]). This is an I/O operation and will block until complete. It must not be called from the main application thread. A blocked call will be canceled with IOException if close() is called from another thread. Requires the NFC permission.

sendDataMessage:  
Send a data based SMS to a specific application port. Note: Using this method requires that your app has the SEND_SMS permission.

captureSingleRequest:  
Submit a request for an image to be captured by the camera device.  The behavior of this method matches that of capture(CaptureRequest, CaptureCallback, Handler), except that it uses Executor as an argument instead of Handler.     See also: captureBurst(List, CameraCaptureSession.CaptureCallback, Handler)setRepeatingRequest(CaptureRequest, CameraCaptureSession.CaptureCallback, Handler)setRepeatingBurst(List, CameraCaptureSession.CaptureCallback, Handler)abortCaptures()createReprocessableCaptureSession(InputConfiguration, List, CameraCaptureSession.StateCallback, Handler)

getMessageId:  
Gets the Message identifier. This provides an index to help with complete Navigation Message assembly. Similar identifiers within the data bits themselves often supplement this information, in ways even more specific to each message type; see the relevant satellite constellation ICDs for details. For GPS L1 C/A subframe 4 and 5, this value corresponds to the 'frame id' of the navigation message, in the range of 1-25 (Subframe 1, 2, 3 does not contain a 'frame id' and this value can be set to -1.)  For Glonass L1 C/A, this refers to the frame ID, in the range of 1-5.  For BeiDou D1, this refers to the frame number in the range of 1-24  For Beidou D2, this refers to the frame number, in the range of 1-120  For Galileo F/NAV nominal frame structure, this refers to the subframe number, in the range of 1-12  For Galileo I/NAV nominal frame structure, this refers to the subframe number in the range of 1-24

clearTestProviderLocation:  
Removes any mock location associated with the given provider.

removeGpsData:  
Removes GPS latitude, longitude, altitude, and timestamp from the parameters.

sendConnectionEvent:  
Sends an event associated with this Connection with associated event extras to the InCallService. Connection events are used to communicate point in time information from a ConnectionService to a InCallService implementations.  An example of a custom connection event includes notifying the UI when a WIFI call has been handed over to LTE, which the InCall UI might use to inform the user that billing charges may apply.  The Android Telephony framework will send the EVENT_CALL_MERGE_FAILED connection event when a call to mergeConference() has failed to complete successfully.  A connection event could also be used to trigger UI in the InCallService which prompts the user to make a choice (e.g. whether they want to incur roaming costs for making a call), which is communicated back via sendCallEvent(String, Bundle). Events are exposed to InCallService implementations via onConnectionEvent(Call, String, Bundle). No assumptions should be made as to how an In-Call UI or service will handle these events. The ConnectionService must assume that the In-Call UI could even chose to ignore some events altogether. Events should be fully qualified (e.g. com.example.event.MY_EVENT) to avoid conflicts between ConnectionService implementations.  Further, custom ConnectionService implementations shall not re-purpose events in the android.* namespace, nor shall they define new event types in this namespace.  When defining a custom event type, ensure the contents of the extras Bundle is clearly defined.  Extra keys for this bundle should be named similar to the event type (e.g. com.example.extra.MY_EXTRA). When defining events and the associated extras, it is important to keep their behavior consistent when the associated ConnectionService is updated.  Support for deprecated events/extras should me maintained to ensure backwards compatibility with older InCallService implementations which were built to support the older behavior.

setAudioRoute:  
Sets the audio route (speaker, bluetooth, etc...).  When this request is honored, there will be change to the getCallAudioState(). Used by self-managed ConnectionServices which wish to change the audio route for a self-managed Connection (see CAPABILITY_SELF_MANAGED.) See also setAudioRoute(int).

stopScan:  
Stops an ongoing Bluetooth LE scan. Requires the BLUETOOTH_ADMIN permission.

ignore:  
Signals that you are no longer interested in communicating with an NFC tag for as long as it remains in range. All future attempted communication to this tag will fail with IOException. The NFC controller will be put in a low-power polling mode, allowing the device to save power in cases where it's "attached" to a tag all the time (e.g. a tag in car dock). Additionally the debounceMs parameter allows you to specify for how long the tag needs to have gone out of range, before it will be dispatched again. Note: the NFC controller typically polls at a pretty slow interval (100 - 500 ms). This means that if the tag repeatedly goes in and out of range (for example, in case of a flaky connection), and the controller happens to poll every time the tag is out of range, it *will* re-dispatch the tag after debounceMs, despite the tag having been "in range" during the interval. Note 2: if a tag with another UID is detected after this API is called, its effect will be cancelled; if this tag shows up before the amount of time specified in debounceMs, it will be dispatched again. Note 3: some tags have a random UID, in which case this API won't work reliably.

requestSingleUpdate:  
Register for a single location update using a Criteria and pending intent. See requestLocationUpdates(long, float, Criteria, PendingIntent) for more detail on how to use this method. Requires the ACCESS_COARSE_LOCATION or ACCESS_FINE_LOCATION permissions.

setTorchMode:  
Set the flash unit's torch mode of the camera of the given ID without opening the camera device. Use getCameraIdList() to get the list of available camera devices and use getCameraCharacteristics(String) to check whether the camera device has a flash unit. Note that even if a camera device has a flash unit, turning on the torch mode may fail if the camera device or other camera resources needed to turn on the torch mode are in use.  If setTorchMode(String, boolean) is called to turn on or off the torch mode successfully, onTorchModeChanged(String, boolean) will be invoked. However, even if turning on the torch mode is successful, the application does not have the exclusive ownership of the flash unit or the camera device. The torch mode will be turned off and becomes unavailable when the camera device that the flash unit belongs to becomes unavailable or when other camera resources to keep the torch on become unavailable ( onTorchModeUnavailable(String) will be invoked). Also, other applications are free to call setTorchMode(String, boolean) to turn off the torch mode ( onTorchModeChanged(String, boolean) will be invoked). If the latest application that turned on the torch mode exits, the torch mode will be turned off.

requestLocationUpdates:  
Register for location updates using the named provider, and a pending intent. See requestLocationUpdates(long, float, Criteria, PendingIntent) for more detail on how to use this method. Requires the ACCESS_COARSE_LOCATION or ACCESS_FINE_LOCATION permissions.

registerTorchCallback:  
Register a callback to be notified about torch mode status. Registering the same callback again will replace the handler with the new one provided.  The first time a callback is registered, it is immediately called with the torch mode status of all currently known camera devices with a flash unit.  Since this callback will be registered with the camera service, remember to unregister it once it is no longer needed; otherwise the callback will continue to receive events indefinitely and it may prevent other resources from being released. Specifically, the callbacks will be invoked independently of the general activity lifecycle and independently of the state of individual CameraManager instances.

onDownloadMms:  
Override this method to download MMSs received.

isSipWifiOnly:  
Returns true if SIP is only available on WIFI.

showAsDropDown:  
Displays the content view in a popup window anchored to the corner of another view. The window is positioned according to the specified gravity and offset by the specified x and y coordinates. If there is not enough room on screen to show the popup in its entirety, this method tries to find a parent scroll view to scroll. If no parent view can be scrolled, the specified vertical gravity will be ignored and the popup will anchor itself such that it is visible. If the view later scrolls to move anchor to a different location, the popup will be moved correspondingly.   See also: dismiss()

connectionServiceFocusReleased:  
Call to inform Telecom that your ConnectionService has released call resources (e.g microphone, camera).  See also: onConnectionServiceFocusLost()

hasSigningCertificate:  
Searches the set of signing certificates by which the package(s) for the given uid has proven to have been signed.  For multiple packages sharing the same uid, this will return the signing certificates found in the signing history of the "newest" package, where "newest" indicates the package with the newest signing certificate in the shared uid group.  This method should be used instead of getPackageInfo with GET_SIGNATURES since it takes into account the possibility of signing certificate rotation, except in the case of packages that are signed by multiple certificates, for which signing certificate rotation is not supported. This method is analogous to using getPackagesForUid followed by getPackageInfo with GET_SIGNING_CERTIFICATES, selecting the PackageInfo of the newest-signed bpackage , and finally searching through the resulting signingCertificateHistory field to see if the desired certificate is there.

clone:  
Clone the history item for use by clients of WebView.

getCameraInfo:  
Returns the information about a particular camera. If getNumberOfCameras() returns N, the valid id is 0 to N-1.

getAllowed:  
Gets the Geolocation permission state for the specified origin.

NeighboringCellInfo:  
Initialize the object from rssi, location string, and radioType radioType is one of following TelephonyManager.NETWORK_TYPE_GPRS, TelephonyManager.NETWORK_TYPE_EDGE, TelephonyManager.NETWORK_TYPE_UMTS, TelephonyManager.NETWORK_TYPE_HSDPA, TelephonyManager.NETWORK_TYPE_HSUPA, and TelephonyManager.NETWORK_TYPE_HSPA.

checkBluetoothAddress:  
Validate a String Bluetooth address, such as "00:43:A8:23:10:F0" Alphabetic characters must be uppercase to be valid.

autoFocus:  
Starts camera auto-focus and registers a callback function to run when the camera is focused.  This method is only valid when preview is active (between startPreview() and before stopPreview()). Callers should check getFocusMode() to determine if this method should be called. If the camera does not support auto-focus, it is a no-op and onAutoFocus(boolean, Camera) callback will be called immediately. If your application should not be installed on devices without auto-focus, you must declare that your application uses auto-focus with the <uses-feature> manifest element.  If the current flash mode is not FLASH_MODE_OFF, flash may be fired during auto-focus, depending on the driver and camera hardware.  Auto-exposure lock getAutoExposureLock() and auto-white balance locks getAutoWhiteBalanceLock() do not change during and after autofocus. But auto-focus routine may stop auto-exposure and auto-white balance transiently during focusing. Stopping preview with stopPreview(), or triggering still image capture with takePicture(Camera.ShutterCallback, Camera.PictureCallback, Camera.PictureCallback), will not change the the focus position. Applications must call cancelAutoFocus to reset the focus.  If autofocus is successful, consider using MediaActionSound to properly play back an autofocus success sound to the user.    See also: cancelAutoFocus()setAutoExposureLock(boolean)setAutoWhiteBalanceLock(boolean)MediaActionSound

connect:  
Enable I/O operations to the tag from this TagTechnology object. May cause RF activity and may block. Must not be called from the main application thread. A blocked call will be canceled with IOException by calling close() from another thread. Only one TagTechnology object can be connected to a Tag at a time. Applications must call close() when I/O operations are complete. Requires the NFC permission.

assertBaselineAligned:  
Assert that two views are aligned on their baseline, that is that their baselines are on the same y location.

getSubElementOffsetBytes:  
This function specifies the location of a sub-element within the element

sendMultimediaMessage:  
Send an MMS message

BluetoothHidDeviceAppQosSettings:  
Create a BluetoothHidDeviceAppQosSettings object for the Bluetooth L2CAP channel. The QoS Settings is optional. Please refer to Bluetooth HID Specfication v1.1.1 Section 5.2 and Appendix D for parameters.

getSecondaryHorizontal:  
Get the secondary horizontal position for the specified text offset. This is the location where a new character would be inserted in the direction other than the paragraph's primary direction.

getSendStatus:  
Returns the send status of the just-sent SMS.

setPreviewSurface:  
Sets the surface to be used for displaying a preview of what the user's camera is currently capturing.  When video transmission is enabled, this is the video signal which is sent to the remote device. Handled by onSetPreviewSurface(Surface).

transceive:  
Send raw NFC-F commands to the tag and receive the response. Applications must not prefix the SoD (preamble and sync code) and/or append the EoD (CRC) to the payload, it will be automatically calculated. A typical NFC-F frame for this method looks like: LENGTH (1 byte) --- CMD (1 byte) -- IDm (8 bytes) -- PARAMS (LENGTH - 10 bytes)  Use getMaxTransceiveLength() to retrieve the maximum amount of bytes that can be sent with transceive(byte[]). This is an I/O operation and will block until complete. It must not be called from the main application thread. A blocked call will be canceled with IOException if close() is called from another thread. Requires the NFC permission.

removeTestProvider:  
Removes the mock location provider with the given name.

set:  
Set a capture request field to a value. The field definitions can be found in CaptureRequest. Setting a field to null will remove that field from the capture request. Unless the field is optional, removing it will likely produce an error from the camera device when the request is submitted.

CarrierMessagingService.SendSmsResult:  
Constructs a SendSmsResult with the send status and message reference for the just-sent SMS.

isExtendedLengthApduSupported:  
Standard APDUs have a 1-byte length field, allowing a maximum of 255 payload bytes, which results in a maximum APDU length of 261 bytes. Extended length APDUs have a 3-byte length field, allowing 65535 payload bytes. Some NFC adapters, like the one used in the Nexus S and the Galaxy Nexus do not support extended length APDUs. They are expected to be well-supported in the future though. Use this method to check for extended length APDU support.

forEach:  
Apply the filter to the input and save to the specified allocation.

onCaptureBufferLost:  
This method is called if a single buffer for a capture could not be sent to its destination surface.  If the whole capture failed, then onCaptureFailed(CameraCaptureSession, CaptureRequest, CaptureFailure) will be called instead. If some but not all buffers were captured but the result metadata will not be available, then onCaptureFailed will be invoked with wasImageCaptured() returning true, along with one or more calls to onCaptureBufferLost(CameraCaptureSession, CaptureRequest, Surface, long) for the failed outputs.

setGpsAltitude:  
Sets GPS altitude. This will be stored in JPEG EXIF header.

getFocusDistances:  
Gets the distances from the camera to where an object appears to be in focus. The object is sharpest at the optimal focus distance. The depth of field is the far focus distance minus near focus distance.  Focus distances may change after calling autoFocus(AutoFocusCallback), cancelAutoFocus(), or startPreview(). Applications can call getParameters() and this method anytime to get the latest focus distances. If the focus mode is FOCUS_MODE_CONTINUOUS_VIDEO, focus distances may change from time to time.  This method is intended to estimate the distance between the camera and the subject. After autofocus, the subject distance may be within near and far focus distance. However, the precision depends on the camera hardware, autofocus algorithm, the focus area, and the scene. The error can be large and it should be only used as a reference.  Far focus distance >= optimal focus distance >= near focus distance. If the focus distance is infinity, the value will be Float.POSITIVE_INFINITY.   See also: FOCUS_DISTANCE_NEAR_INDEXFOCUS_DISTANCE_OPTIMAL_INDEXFOCUS_DISTANCE_FAR_INDEX

registerGnssStatusCallback:  
Registers a GNSS status callback. Requires the ACCESS_FINE_LOCATION permission.

onReceiveTextSms:  
Override this method to filter inbound SMS messages. This method will be called once for every incoming text SMS. You can invoke the callback with a bitmask to tell the platform how to handle the SMS. For a SMS received on a file-based encryption capable device while the credential-encrypted storage is not available, this method will be called for the second time when the credential-encrypted storage becomes available after the user unlocks the phone, if the bit RECEIVE_OPTIONS_DROP is not set when invoking the callback.

setHotspot:  
Specifies the hotspot's location within the drawable.

setTorchMode:  
Set the flash unit's torch mode of the camera of the given ID without opening the camera device. Use getCameraIdList() to get the list of available camera devices and use getCameraCharacteristics(String) to check whether the camera device has a flash unit. Note that even if a camera device has a flash unit, turning on the torch mode may fail if the camera device or other camera resources needed to turn on the torch mode are in use.  If setTorchMode(String, boolean) is called to turn on or off the torch mode successfully, onTorchModeChanged(String, boolean) will be invoked. However, even if turning on the torch mode is successful, the application does not have the exclusive ownership of the flash unit or the camera device. The torch mode will be turned off and becomes unavailable when the camera device that the flash unit belongs to becomes unavailable or when other camera resources to keep the torch on become unavailable ( onTorchModeUnavailable(String) will be invoked). Also, other applications are free to call setTorchMode(String, boolean) to turn off the torch mode ( onTorchModeChanged(String, boolean) will be invoked). If the latest application that turned on the torch mode exits, the torch mode will be turned off.

forEach_Dot:  
Process an input buffer and place the histogram into the output allocation. The dot product of the input channel and the coefficients from 'setDotCoefficients' are used to calculate the output values. 1D and 2D input allocations are supported.

clone:  
Clone the history item for use by clients of WebView.

NdefRecord:  
Construct an NDEF Record from its component fields. Recommend to use helpers such as {#createUri} or {createExternal(String, String, byte[]) where possible, since they perform stricter validation that the record is correctly formatted as per NDEF specifications. However if you know what you are doing then this constructor offers the most flexibility. An NdefRecord represents a logical (complete) record, and cannot represent NDEF Record chunks. Basic validation of the tnf, type, id and payload is performed as per the following rules: The tnf paramter must be a 3-bit value. Records with a tnf of TNF_EMPTY cannot have a type, id or payload. Records with a tnf of TNF_UNKNOWN or 0x07 cannot have a type. Records with a tnf of TNF_UNCHANGED are not allowed since this class only represents complete (unchunked) records. This minimal validation is specified by NFCForum-TS-NDEF_1.0 section 3.2.6 (Type Name Format). If any of the above validation steps fail then IllegalArgumentException is thrown. Deep inspection of the type, id and payload fields is not performed, so it is possible to create NDEF Records that conform to section 3.2.6 but fail other more strict NDEF specification requirements. For example, the payload may be invalid given the tnf and type. To omit a type, id or payload field, set the parameter to an empty byte array or null.

sendExtraCommand:  
Sends additional commands to a location provider. Can be used to support provider specific extensions to the Location Manager API

SparseArray:  
Creates a new SparseArray containing no mappings that will not require any additional memory allocation to store the specified number of mappings.  If you supply an initial capacity of 0, the sparse array will be initialized with a light-weight representation not requiring any additional array allocations.

SparseArray:  
Creates a new SparseArray containing no mappings that will not require any additional memory allocation to store the specified number of mappings.  If you supply an initial capacity of 0, the sparse array will be initialized with a light-weight representation not requiring any additional array allocations.

getTime:  
Return the UTC time of this fix, in milliseconds since January 1, 1970. Note that the UTC time on a device is not monotonic: it can jump forwards or backwards unpredictably. So always use getElapsedRealtimeNanos() when calculating time deltas. On the other hand, getTime() is useful for presenting a human readable time to the user, or for carefully comparing location fixes across reboot or across devices. All locations generated by the LocationManager are guaranteed to have a valid UTC time, however remember that the system time may have changed since the location was generated.

update:  
Updates the position and the dimension of the popup window. Width and height can be set to -1 to update location only. Calling this function also updates the window with the current popup state as described for update(). If the view later scrolls to move anchor to a different location, the popup will be moved correspondingly.

setAccuracy:  
Set the estimated horizontal accuracy of this location, meters. See getAccuracy() for the definition of horizontal accuracy. Following this call hasAccuracy() will return true.

getAccuracy:  
Returns a constant indicating desired accuracy of location Accuracy may be ACCURACY_FINE if desired location is fine, else it can be ACCURACY_COARSE.

setShareHistoryFileName:  
Sets the file name of a file for persisting the share history which history will be used for ordering share targets. This file will be used for all view created by onCreateActionView(). Defaults to DEFAULT_SHARE_HISTORY_FILE_NAME. Set to null if share history should not be persisted between sessions. Note: The history file name can be set any time, however only the action views created by onCreateActionView() after setting the file name will be backed by the provided file. Therefore, if you want to use different history files for sharing specific types of content, every time you change the history file setShareHistoryFileName(String) you must call invalidateOptionsMenu() to recreate the action view. You should not call invalidateOptionsMenu() from onCreateOptionsMenu(Menu).  private void doShare(Intent intent) {     if (IMAGE.equals(intent.getMimeType())) {         mShareActionProvider.setHistoryFileName(SHARE_IMAGE_HISTORY_FILE_NAME);     } else if (TEXT.equals(intent.getMimeType())) {         mShareActionProvider.setHistoryFileName(SHARE_TEXT_HISTORY_FILE_NAME);     }     mShareActionProvider.setIntent(intent);     invalidateOptionsMenu(); }

distanceTo:  
Returns the approximate distance in meters between this location and the given location.  Distance is defined using the WGS84 ellipsoid.

forEach:  
Process an input buffer and place the histogram into the output allocation. The output allocation may be a narrower vector size than the input. In this case the vector size of the output is used to determine how many of the input channels are used in the computation. This is useful if you have an RGBA input buffer but only want the histogram for RGB. 1D and 2D input allocations are supported.

isInvalidatedByBiometricEnrollment:  
Returns true if the key will be invalidated by enrollment of a new fingerprint or removal of all fingerprints.

Camera:  
Creates a new camera, with empty transformations.

onDeactivated:  
This method will be called in two possible scenarios: The NFC link has been deactivated or lost

startScan:  
Start Bluetooth LE scan. The scan results will be delivered through callback. For unfiltered scans, scanning is stopped on screen off to save power. Scanning is resumed when screen is turned on again. To avoid this, do filetered scanning by using proper ScanFilter. An app must hold ACCESS_COARSE_LOCATION or ACCESS_FINE_LOCATION permission in order to get results. Requires the BLUETOOTH_ADMIN permission.

SparseBooleanArray:  
Creates a new SparseBooleanArray containing no mappings that will not require any additional memory allocation to store the specified number of mappings.  If you supply an initial capacity of 0, the sparse array will be initialized with a light-weight representation not requiring any additional array allocations.

add:  
Adds a View to the overlay. The bounds of the added view should be relative to the host view. Any view added to the overlay should be removed when it is no longer needed or no longer visible. Views in the overlay are visual-only; they do not receive input events and do not participate in focus traversal. Overlay views are intended to be transient, such as might be needed by a temporary animation effect.  If the view has a parent, the view will be removed from that parent before being added to the overlay. Also, if that parent is attached in the current view hierarchy, the view will be repositioned such that it is in the same relative location inside the activity. For example, if the view's current parent lies 100 pixels to the right and 200 pixels down from the origin of the overlay's host view, then the view will be offset by (100, 200).  Views added with this API will be drawn in the order they were added. Drawing of the overlay views will happen before drawing of any of the Drawables added with add(Drawable) API even if a call to this API happened after the call to add(Drawable).  Passing null parameter will result in an IllegalArgumentException being thrown.   See also: remove(View)add(Drawable)

setSingleRepeatingRequest:  
Request endlessly repeating capture of images by this capture session. The behavior of this method matches that of setRepeatingRequest(CaptureRequest, CaptureCallback, Handler), except that it uses Executor as an argument instead of Handler.     See also: capture(CaptureRequest, CameraCaptureSession.CaptureCallback, Handler)captureBurst(List, CameraCaptureSession.CaptureCallback, Handler)setRepeatingBurst(List, CameraCaptureSession.CaptureCallback, Handler)stopRepeating()abortCaptures()

getProfileProxy:  
Get the profile proxy object associated with the profile. Profile can be one of HEALTH, HEADSET, A2DP, GATT, or GATT_SERVER. Clients must implement BluetoothProfile.ServiceListener to get notified of the connection status and to get the proxy object.

getData:  
Gets the data of the reported GPS message. The bytes (or words) specified using big endian format (MSB first). For GPS L1 C/A, Beidou D1 & Beidou D2, each subframe contains 10 30-bit words. Each word (30 bits) should be fit into the last 30 bits in a 4-byte word (skip B31 and B32), with MSB first, for a total of 40 bytes, covering a time period of 6, 6, and 0.6 seconds, respectively. For Glonass L1 C/A, each string contains 85 data bits, including the checksum.  These bits should be fit into 11 bytes, with MSB first (skip B86-B88), covering a time period of 2 seconds. For Galileo F/NAV, each word consists of 238-bit (sync & tail symbols excluded). Each word should be fit into 30-bytes, with MSB first (skip B239, B240), covering a time period of 10 seconds. For Galileo I/NAV, each page contains 2 page parts, even and odd, with a total of 2x114 = 228 bits, (sync & tail excluded) that should be fit into 29 bytes, with MSB first (skip B229-B232).

reconfigure:  
Modifies the bitmap to have a specified width, height, and Bitmap.Config, without affecting the underlying allocation backing the bitmap. Bitmap pixel data is not re-initialized for the new configuration.  This method can be used to avoid allocating a new bitmap, instead reusing an existing bitmap's allocation for a new configuration of equal or lesser size. If the Bitmap's allocation isn't large enough to support the new configuration, an IllegalArgumentException will be thrown and the bitmap will not be modified.  The result of getByteCount() will reflect the new configuration, while getAllocationByteCount() will reflect that of the initial configuration.  Note: This may change this result of hasAlpha(). When converting to 565, the new bitmap will always be considered opaque. When converting from 565, the new bitmap will be considered non-opaque, and will respect the value set by setPremultiplied().  WARNING: This method should NOT be called on a bitmap currently in use by the view system, Canvas, or the AndroidBitmap NDK API. It does not make guarantees about how the underlying pixel buffer is remapped to the new config, just that the allocation is reused. Additionally, the view system does not account for bitmap properties being modifying during use, e.g. while attached to drawables.  In order to safely ensure that a Bitmap is no longer in use by the View system it is necessary to wait for a draw pass to occur after invalidate()'ing any view that had previously drawn the Bitmap in the last draw pass due to hardware acceleration's caching of draw commands. As an example, here is how this can be done for an ImageView: ImageView myImageView = ...;      final Bitmap myBitmap = ...;      myImageView.setImageDrawable(null);      myImageView.post(new Runnable() {          public void run() {              // myBitmap is now no longer in use by the ImageView              // and can be safely reconfigured.              myBitmap.reconfigure(...);          }      });   See also: setWidth(int)setHeight(int)setConfig(Config)

getRowBytes:  
Return the number of bytes between rows in the bitmap's pixels. Note that this refers to the pixels as stored natively by the bitmap. If you call getPixels() or setPixels(), then the pixels are uniformly treated as 32bit values, packed according to the Color class. As of KITKAT, this method should not be used to calculate the memory usage of the bitmap. Instead, see getAllocationByteCount().

getSvid:  
Gets the identification number for the satellite at the specific index. This svid is pseudo-random number for most constellations. It is FCN & OSN number for Glonass. The distinction is made by looking at constellation field getConstellationType(int) Expected values are in the range of: GPS: 1-32 SBAS: 120-151, 183-192 GLONASS: One of: OSN, or FCN+100  1-24 as the orbital slot number (OSN) (preferred, if known) 93-106 as the frequency channel number (FCN) (-7 to +6) plus 100.   i.e. encode FCN of -7 as 93, 0 as 100, and +6 as 106  QZSS: 193-200 Galileo: 1-36 Beidou: 1-37

setRepeatingBurstRequests:  
Request endlessly repeating capture of a sequence of images by this capture session.  The behavior of this method matches that of setRepeatingBurst(List, CaptureCallback, Handler), except that it uses Executor as an argument instead of Handler.     See also: capture(CaptureRequest, CameraCaptureSession.CaptureCallback, Handler)captureBurst(List, CameraCaptureSession.CaptureCallback, Handler)setRepeatingRequest(CaptureRequest, CameraCaptureSession.CaptureCallback, Handler)stopRepeating()abortCaptures()

captureSingleRequest:  
Submit a request for an image to be captured by the camera device.  The behavior of this method matches that of capture(CaptureRequest, CaptureCallback, Handler), except that it uses Executor as an argument instead of Handler.     See also: captureBurst(List, CameraCaptureSession.CaptureCallback, Handler)setRepeatingRequest(CaptureRequest, CameraCaptureSession.CaptureCallback, Handler)setRepeatingBurst(List, CameraCaptureSession.CaptureCallback, Handler)abortCaptures()createReprocessableCaptureSession(InputConfiguration, List, CameraCaptureSession.StateCallback, Handler)

SessionConfiguration:  
Create a new SessionConfiguration.   See also: SESSION_REGULARSESSION_HIGH_SPEEDcreateCaptureSession(List, CameraCaptureSession.StateCallback, Handler)createCaptureSessionByOutputConfigurations(List, CameraCaptureSession.StateCallback, Handler)createReprocessableCaptureSession(InputConfiguration, List, CameraCaptureSession.StateCallback, Handler)createConstrainedHighSpeedCaptureSession(List, CameraCaptureSession.StateCallback, Handler)

onLocationChanged:  
Called when the location has changed. There are no restrictions on the use of the supplied Location object.

toByteArray:  
Return this NDEF Message as raw bytes. The NDEF Message is formatted as per the NDEF 1.0 specification, and the byte array is suitable for network transmission or storage in an NFC Forum NDEF compatible tag. This method will not chunk any records, and will always use the short record (SR) format and omit the identifier field when possible.   See also: ERROR(/getByteArrayLength)

getSpeed:  
Get the speed if it is available, in meters/second over ground. If this location does not have a speed then 0.0 is returned.

processCommandApdu:  
This method will be called when a command APDU has been received from a remote device. A response APDU can be provided directly by returning a byte-array in this method. Note that in general response APDUs must be sent as quickly as possible, given the fact that the user is likely holding his device over an NFC reader when this method is called. If there are multiple services that have registered for the same AIDs in their meta-data entry, you will only get called if the user has explicitly selected your service, either as a default or just for the next tap. This method is running on the main thread of your application. If you cannot return a response APDU immediately, return null and use the sendResponseApdu(byte[]) method later.

drag:  
Simulate touching a specific location and dragging to a new location.

ignore:  
Signals that you are no longer interested in communicating with an NFC tag for as long as it remains in range. All future attempted communication to this tag will fail with IOException. The NFC controller will be put in a low-power polling mode, allowing the device to save power in cases where it's "attached" to a tag all the time (e.g. a tag in car dock). Additionally the debounceMs parameter allows you to specify for how long the tag needs to have gone out of range, before it will be dispatched again. Note: the NFC controller typically polls at a pretty slow interval (100 - 500 ms). This means that if the tag repeatedly goes in and out of range (for example, in case of a flaky connection), and the controller happens to poll every time the tag is out of range, it *will* re-dispatch the tag after debounceMs, despite the tag having been "in range" during the interval. Note 2: if a tag with another UID is detected after this API is called, its effect will be cancelled; if this tag shows up before the amount of time specified in debounceMs, it will be dispatched again. Note 3: some tags have a random UID, in which case this API won't work reliably.

disable:  
Turn off the local Bluetooth adapter！do not use without explicit user action to turn off Bluetooth. This gracefully shuts down all Bluetooth connections, stops Bluetooth system services, and powers down the underlying Bluetooth hardware. Bluetooth should never be disabled without direct user consent. The disable() method is provided only for applications that include a user interface for changing system settings, such as a "power manager" app.  This is an asynchronous call: it will return immediately, and clients should listen for ACTION_STATE_CHANGED to be notified of subsequent adapter state changes. If this call returns true, then the adapter state will immediately transition from STATE_ON to STATE_TURNING_OFF, and some time later transition to either STATE_OFF or STATE_ON. If this call returns false then there was an immediate problem that will prevent the adapter from being turned off - such as the adapter already being turned off. Requires the BLUETOOTH_ADMIN permission.

flushPendingScanResults:  
Flush pending batch scan results stored in Bluetooth controller. This will return Bluetooth LE scan results batched on bluetooth controller. Returns immediately, batch scan results data will be delivered through the callback.

setAccuracy:  
Indicates the desired accuracy for latitude and longitude. Accuracy may be ACCURACY_FINE if desired location is fine, else it can be ACCURACY_COARSE. More accurate location may consume more power and may take longer.

close:  
Disable I/O operations to the tag from this TagTechnology object, and release resources. Also causes all blocked I/O operations on other thread to be canceled and return with IOException. Requires the NFC permission.

getAccuracy:  
Returns a constant describing horizontal accuracy of this provider. If the provider returns finer grain or exact location, ACCURACY_FINE is returned, otherwise if the location is only approximate then ACCURACY_COARSE is returned.

getFullBiasNanos:  
Gets the difference between hardware clock (getTimeNanos()) inside GPS receiver and the true GPS time since 0000Z, January 6, 1980, in nanoseconds. This value is available if the receiver has estimated GPS time. If the computed time is for a non-GPS constellation, the time offset of that constellation to GPS has to be applied to fill this value. The value is only available if hasFullBiasNanos() is true. The error estimate for the sum of this field and getBiasNanos() is getBiasUncertaintyNanos(). The sign of the value is defined by the following equation: local estimate of GPS time = TimeNanos - (FullBiasNanos + BiasNanos)

SparseLongArray:  
Creates a new SparseLongArray containing no mappings that will not require any additional memory allocation to store the specified number of mappings.  If you supply an initial capacity of 0, the sparse array will be initialized with a light-weight representation not requiring any additional array allocations.

setLookasideConfig:  
Configures lookaside memory allocator This method should be called from the constructor of the subclass, before opening the database, since lookaside memory configuration can only be changed when no connection is using it SQLite default settings will be used, if this method isn't called. Use setLookasideConfig(0,0) to disable lookaside Note: Provided slotSize/slotCount configuration is just a recommendation. The system may choose different values depending on a device, e.g. lookaside allocations can be disabled on low-RAM devices

onUpdateCursorAnchorInfo:  
Called when the application has reported a new location of its text insertion point and characters in the composition string.  This is only called if explicitly requested by the input method. The default implementation does nothing.

VideoProfile.CameraCapabilities:  
Create a call camera capabilities instance.

connect:  
Start a p2p connection to a device with the specified configuration. The function call immediately returns after sending a connection request to the framework. The application is notified of a success or failure to initiate connect through listener callbacks onSuccess() or onFailure(int). Register for WIFI_P2P_CONNECTION_CHANGED_ACTION intent to determine when the framework notifies of a change in connectivity. If the current device is not part of a p2p group, a connect request initiates a group negotiation with the peer. If the current device is part of an existing p2p group or has created a p2p group with createGroup(WifiP2pManager.Channel, WifiP2pManager.ActionListener), an invitation to join the group is sent to the peer device.

getHeight:  
The height of the camera video in pixels.

onProvideShadowMetrics:  
Provides the metrics for the shadow image. These include the dimensions of the shadow image, and the point within that shadow that should be centered under the touch location while dragging. The default implementation sets the dimensions of the shadow to be the same as the dimensions of the View itself and centers the shadow under the touch point.

createGroup:  
Create a p2p group with the current device as the group owner. This essentially creates an access point that can accept connections from legacy clients as well as other p2p devices. Note: This function would normally not be used unless the current device needs to form a p2p connection with a legacy client The function call immediately returns after sending a group creation request to the framework. The application is notified of a success or failure to initiate group creation through listener callbacks onSuccess() or onFailure(int). Application can request for the group details with requestGroupInfo(WifiP2pManager.Channel, WifiP2pManager.GroupInfoListener).

allocateBytes:  
Allocate the requested number of bytes for your application to use in the given open file. This will cause the system to delete any cached files necessary to satisfy your request. Attempts to allocate disk space beyond the value returned by getAllocatableBytes(UUID) will fail. This method guarantees that bytes have been allocated to the opened file, otherwise it will throw if fast allocation is not possible. Fast allocation is typically only supported in private app data directories, and on shared/external storage devices which are emulated. If you're progressively allocating an unbounded amount of storage space (such as when recording a video) you should avoid calling this method more than once every 60 seconds. This method may take several seconds to complete, so it should            only be called from a worker thread.    See also: ERROR(/#getAllocatableBytes(UUID, int))isAllocationSupported(FileDescriptor)isExternalStorageEmulated(File)

connect:  
Enable I/O operations to the tag from this TagTechnology object. May cause RF activity and may block. Must not be called from the main application thread. A blocked call will be canceled with IOException by calling close() from another thread. Only one TagTechnology object can be connected to a Tag at a time. Applications must call close() when I/O operations are complete. Requires the NFC permission.

setPreviewCallbackWithBuffer:  
Installs a callback to be invoked for every preview frame, using buffers supplied with addCallbackBuffer(byte[]), in addition to displaying them on the screen.  The callback will be repeatedly called for as long as preview is active and buffers are available.  Any other preview callbacks are overridden.  The purpose of this method is to improve preview efficiency and frame rate by allowing preview frame memory reuse.  You must call addCallbackBuffer(byte[]) at some point -- before or after calling this method -- or no callbacks will received.  The buffer queue will be cleared if this method is called with a null callback, setPreviewCallback(Camera.PreviewCallback) is called, or setOneShotPreviewCallback(Camera.PreviewCallback) is called.  If you are using the preview data to create video or still images, strongly consider using MediaActionSound to properly indicate image capture or recording start/stop to the user.    See also: addCallbackBuffer(byte[])MediaActionSound

close:  
Disable I/O operations to the tag from this TagTechnology object, and release resources. Also causes all blocked I/O operations on other thread to be canceled and return with IOException. Requires the NFC permission.

OutputConfiguration:  
Create a new OutputConfiguration instance with a Surface, with a surface group ID. A surface group ID is used to identify which surface group this output surface belongs to. A surface group is a group of output surfaces that are not intended to receive camera output buffer streams simultaneously. The CameraDevice may be able to share the buffers used by all the surfaces from the same surface group, therefore may reduce the overall memory footprint. The application should only set the same set ID for the streams that are not simultaneously streaming. A negative ID indicates that this surface doesn't belong to any surface group. The default value is .SURFACE_GROUP_ID_NONE.  For example, a video chat application that has an adaptive output resolution feature would need two (or more) output resolutions, to switch resolutions without any output glitches. However, at any given time, only one output is active to minimize outgoing network bandwidth and encoding overhead.  To save memory, the application should set the video outputs to have the same non-negative group ID, so that the camera device can share the same memory region for the alternating outputs.  It is not an error to include output streams with the same group ID in the same capture request, but the resulting memory consumption may be higher than if the two streams were not in the same surface group to begin with, especially if the outputs have substantially different dimensions.

onSharedElementsArrived:  
Called during an Activity Transition when the shared elements have arrived at the final location and are ready to be transferred. This method is called for both the source and destination Activities. When the shared elements are ready to be transferred, onSharedElementsReady() must be called to trigger the transfer. The default behavior is to trigger the transfer immediately.

hasProfile:  
Returns true if camcorder profile exists for the given camera at the given quality level. When using the Camera 2 API in LEGACY mode (i.e. when INFO_SUPPORTED_HARDWARE_LEVEL is set to INFO_SUPPORTED_HARDWARE_LEVEL_LEGACY), hasProfile(int) may return true for unsupported resolutions.  To ensure a a given resolution is supported in LEGACY mode, the configuration given in SCALER_STREAM_CONFIGURATION_MAP must contain the the resolution in the supported output sizes.  The recommended way to check this is with getOutputSizes(Class) with the class of the desired recording endpoint, and check that the desired resolution is contained in the list returned.    See also: CameraManagerCameraCharacteristics

makeReadOnly:  
Make a tag read-only. This sets the CC field to indicate the tag is read-only, and where possible permanently sets the lock bits to prevent any further modification of the memory. This is a one-way process and cannot be reverted! This is an I/O operation and will block until complete. It must not be called from the main application thread. A blocked call will be canceled with IOException if close() is called from another thread. Requires the NFC permission.

NdefRecord:  
Construct an NDEF Record from its component fields. Recommend to use helpers such as {#createUri} or {createExternal(String, String, byte[]) where possible, since they perform stricter validation that the record is correctly formatted as per NDEF specifications. However if you know what you are doing then this constructor offers the most flexibility. An NdefRecord represents a logical (complete) record, and cannot represent NDEF Record chunks. Basic validation of the tnf, type, id and payload is performed as per the following rules: The tnf paramter must be a 3-bit value. Records with a tnf of TNF_EMPTY cannot have a type, id or payload. Records with a tnf of TNF_UNKNOWN or 0x07 cannot have a type. Records with a tnf of TNF_UNCHANGED are not allowed since this class only represents complete (unchunked) records. This minimal validation is specified by NFCForum-TS-NDEF_1.0 section 3.2.6 (Type Name Format). If any of the above validation steps fail then IllegalArgumentException is thrown. Deep inspection of the type, id and payload fields is not performed, so it is possible to create NDEF Records that conform to section 3.2.6 but fail other more strict NDEF specification requirements. For example, the payload may be invalid given the tnf and type. To omit a type, id or payload field, set the parameter to an empty byte array or null.

takePicture:  
Triggers an asynchronous image capture. The camera service will initiate a series of callbacks to the application as the image capture progresses. The shutter callback occurs after the image is captured. This can be used to trigger a sound to let the user know that image has been captured. The raw callback occurs when the raw image data is available (NOTE: the data will be null if there is no raw image callback buffer available or the raw image callback buffer is not large enough to hold the raw image). The postview callback occurs when a scaled, fully processed postview image is available (NOTE: not all hardware supports this). The jpeg callback occurs when the compressed image is available. If the application does not need a particular callback, a null can be passed instead of a callback method. This method is only valid when preview is active (after startPreview()).  Preview will be stopped after the image is taken; callers must call startPreview() again if they want to re-start preview or take more pictures. This should not be called between start() and stop(). After calling this method, you must not call startPreview() or take another picture until the JPEG callback has returned.

setSessionParameters:  
Sets the session wide camera parameters (see CaptureRequest). This argument can be set for every supported session type and will be passed to the camera device as part of the capture session initialization. Session parameters are a subset of the available capture request parameters (see getAvailableSessionKeys()) and their application can introduce internal camera delays. To improve camera performance it is suggested to change them sparingly within the lifetime of the capture session and to pass their initial values as part of this method.

onSurfaceChanged:  
Called when the surface changed size. Called after the surface is created and whenever the OpenGL ES surface size changes. Typically you will set your viewport here. If your camera is fixed then you could also set your projection matrix here: void onSurfaceChanged(GL10 gl, int width, int height) {     gl.glViewport(0, 0, width, height);     // for a fixed camera, set the projection too     float ratio = (float) width / height;     gl.glMatrixMode(GL10.GL_PROJECTION);     gl.glLoadIdentity();     gl.glFrustumf(-ratio, ratio, -1, 1, 1, 10); }

enableShutterSound:  
Enable or disable the default shutter sound when taking a picture.  By default, the camera plays the system-defined camera shutter sound when takePicture(Camera.ShutterCallback, Camera.PictureCallback, Camera.PictureCallback) is called. Using this method, the shutter sound can be disabled. It is strongly recommended that an alternative shutter sound is played in the Camera.ShutterCallback when the system shutter sound is disabled.  Note that devices may not always allow disabling the camera shutter sound. If the shutter sound state cannot be set to the desired value, this method will return false. canDisableShutterSound can be used to determine whether the device will allow the shutter sound to be disabled.     See also: takePicture(Camera.ShutterCallback, Camera.PictureCallback, Camera.PictureCallback)canDisableShutterSoundCamera.ShutterCallback

writeBlock:  
Write 16-byte block. This is an I/O operation and will block until complete. It must not be called from the main application thread. A blocked call will be canceled with IOException if close() is called from another thread. Requires the NFC permission.

enable:  
Turn on the local Bluetooth adapter！do not use without explicit user action to turn on Bluetooth. This powers on the underlying Bluetooth hardware, and starts all Bluetooth system services. Bluetooth should never be enabled without direct user consent. If you want to turn on Bluetooth in order to create a wireless connection, you should use the ACTION_REQUEST_ENABLE Intent, which will raise a dialog that requests user permission to turn on Bluetooth. The enable() method is provided only for applications that include a user interface for changing system settings, such as a "power manager" app.  This is an asynchronous call: it will return immediately, and clients should listen for ACTION_STATE_CHANGED to be notified of subsequent adapter state changes. If this call returns true, then the adapter state will immediately transition from STATE_OFF to STATE_TURNING_ON, and some time later transition to either STATE_OFF or STATE_ON. If this call returns false then there was an immediate problem that will prevent the adapter from being turned on - such as Airplane mode, or the adapter is already turned on. Requires the BLUETOOTH_ADMIN permission.

setServiceResponseListener:  
Register a callback to be invoked on receiving service discovery response. Used only for vendor specific protocol right now. For Bonjour or Upnp, use setDnsSdResponseListeners(WifiP2pManager.Channel, WifiP2pManager.DnsSdServiceResponseListener, WifiP2pManager.DnsSdTxtRecordListener) or setUpnpServiceResponseListener(WifiP2pManager.Channel, WifiP2pManager.UpnpServiceResponseListener) respectively. see discoverServices(WifiP2pManager.Channel, WifiP2pManager.ActionListener) for the detail.

close:  
Disable I/O operations to the tag from this TagTechnology object, and release resources. Also causes all blocked I/O operations on other thread to be canceled and return with IOException. Requires the NFC permission.

distanceBetween:  
Computes the approximate distance in meters between two locations, and optionally the initial and final bearings of the shortest path between them.  Distance and bearing are defined using the WGS84 ellipsoid. The computed distance is stored in results[0].  If results has length 2 or greater, the initial bearing is stored in results[1]. If results has length 3 or greater, the final bearing is stored in results[2].

onStatusChanged:  
Called when the provider status changes. This method is called when a provider is unable to fetch a location or if the provider has recently become available after a period of unavailability.

unlock:  
Unlocks the camera to allow another process to access it. Normally, the camera is locked to the process with an active Camera object until release() is called.  To allow rapid handoff between processes, you can call this method to release the camera temporarily for another process to use; once the other process is done you can call reconnect() to reclaim the camera. This must be done before calling setCamera(Camera). This cannot be called after recording starts. If you are not recording video, you probably do not need this method.

transceive:  
Send raw NFC-V commands to the tag and receive the response. Applications must not append the CRC to the payload, it will be automatically calculated. The application does provide FLAGS, CMD and PARAMETER bytes. Use getMaxTransceiveLength() to retrieve the maximum amount of bytes that can be sent with transceive(byte[]). This is an I/O operation and will block until complete. It must not be called from the main application thread. A blocked call will be canceled with IOException if close() is called from another thread. Requires the NFC permission.

setAutoFocusMoveCallback:  
Sets camera auto-focus move callback.

onCameraAvailable:  
A new camera has become available to use. The default implementation of this method does nothing.

assertTopAligned:  
Assert that two views are top aligned, that is that their top edges are on the same y location.

isEnabled:  
Return true if this NFC Adapter has any features enabled. If this method returns false, the NFC hardware is guaranteed not to generate or respond to any NFC communication over its NFC radio. Applications can use this to check if NFC is enabled. Applications can request Settings UI allowing the user to toggle NFC using:  startActivity(new Intent(Settings.ACTION_NFC_SETTINGS))   See also: ACTION_NFC_SETTINGS

getDefaultSmsSubscriptionId:  
Returns the system's default SMS subscription id. On a data only device or on error, will return INVALID_SUBSCRIPTION_ID.

