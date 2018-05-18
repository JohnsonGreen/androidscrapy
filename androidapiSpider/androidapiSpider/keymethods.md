android.nfc.tech.NfcBarcode---makeReadOnly:  
Make a tag read-only. This sets the CC field to indicate the tag is read-only, and where possible permanently sets the lock bits to prevent any further modification of the memory. This is a one-way process and cannot be reverted! This is an I/O operation and will block until complete. It must not be called from the main application thread. A blocked call will be canceled with IOException if close() is called from another thread. Requires the NFC permission.

java.security.NoSuchProviderException---KeyException:  
Constructs a KeyException with the specified detail message. A detail message is a String that describes this particular exception.

android.telephony.mbms.MbmsDownloadReceiver---DownloadRequest.Builder:  
Builds a new DownloadRequest.

android.bluetooth.BluetoothSocket---BluetoothHidDeviceAppSdpSettings:  
Create a BluetoothHidDeviceAppSdpSettings object for the Bluetooth SDP record.

android.os.UserHandle---execute:  
Executes the given message on the Looper thread this wrapper is attached to. Execution will happen on the Looper's thread (whether it is the current thread or not), but all RuntimeExceptions encountered while executing the message will be thrown on the calling thread.

android.util.MonthDisplayHelper---i:  
Send an INFO log message.

android.database.CursorWrapper---dispatchChange:  
Dispatches a change notification to the observer. Includes the changed content Uri when available. If a Handler was supplied to the ContentObserver constructor, then a call to the onChange(boolean) method is posted to the handler's message queue. Otherwise, the onChange(boolean) method is invoked immediately on this thread.

java.util.concurrent.atomic.AtomicLongFieldUpdater---updateAndGet:  
Atomically updates the element at index i with the results of applying the given function, returning the updated value. The function should be side-effect-free, since it may be re-applied when attempted updates fail due to contention among threads.

android.hardware.TriggerEventListener---registerListener:  
Registers a SensorEventListener for the given sensor at the given sampling frequency and the given maximum reporting latency.    See also: registerListener(SensorEventListener, Sensor, int, int)

java.lang.TypeNotPresentException---ReflectiveOperationException:  
Constructs a new exception with null as its detail message.  The cause is not initialized, and may subsequently be initialized by a call to initCause(Throwable).

android.app.Notification.WearableExtender---Notification.MessagingStyle:  


android.telecom.InCallService.VideoCall---connectionServiceFocusReleased:  
Call to inform Telecom that your ConnectionService has released call resources (e.g microphone, camera).  See also: onConnectionServiceFocusLost()

android.icu.text.Normalizer.QuickCheckResult---clear:  
Clears this MessagePattern. countParts() will return 0.

android.text.InputFilter.AllCaps---DynamicLayout:  
This constructor was deprecated      in API level P.    Use DynamicLayout.Builder instead.

android.content.pm.PermissionInfo---getPackageUid:  
Return the UID associated with the given package name. Note that the same package will have different UIDs under different UserHandle on the same device.

android.renderscript.ScriptIntrinsicConvolve3x3---forEach:  
Invoke the kernel and apply the lookup to each cell of ain and copy to aout.

android.os.DropBoxManager---resetAllCounts:  
This method was deprecated      in API level 23.    Accurate counting is a burden on the runtime and may be removed.  Clears all the global and thread-local memory allocation counters.  See also: startAllocCounting()

android.service.media.MediaBrowserService.Result---onPrewarm:  
Called when the camera should be prewarmed.

java.lang.InterruptedException---IllegalMonitorStateException:  
Constructs an IllegalMonitorStateException with the specified detail message.

android.media.MediaDrm.HdcpLevel---removeBearing:  
This method was deprecated      in API level 26.    use a new Location object for location updates.  Remove the bearing from this location. Following this call hasBearing() will return false, and getBearing() will return 0.0.

android.telecom.TelecomManager---setPreviewSurface:  
Sets the surface to be used for displaying a preview of what the user's camera is currently capturing for the RemoteConnection.VideoProvider.   See also: onSetPreviewSurface(Surface)

android.media.RemoteControlClient.MetadataEditor---getType:  
Returns the device type identifier of the microphone (e.g AudioDeviceInfo.TYPE_BUILTIN_MIC).

android.app.NotificationChannel---Notification.MessagingStyle.Message:  
Constructor

java.util.concurrent.atomic.DoubleAccumulator---AtomicReference:  
Creates a new AtomicReference with null initial value.

android.telephony.mbms.DownloadStateCallback---SmsMessage:  
This constructor was deprecated      in API level 4.    Use android.telephony.SmsMessage.

java.lang.Deprecated---UnsupportedEncodingException:  
Constructs an UnsupportedEncodingException without a detail message.

android.hardware.camera2.CaptureResult---getSequenceId:  
The sequence ID for this failed capture that was returned by the capture(CaptureRequest, CameraCaptureSession.CaptureCallback, Handler) family of functions. The sequence ID is a unique monotonically increasing value starting from 0, incremented every time a new group of requests is submitted to the CameraDevice.   See also: ERROR(/CameraDevice.CaptureCallback#onCaptureSequenceCompleted)

android.service.autofill.Transformation---UserNotAuthenticatedException:  
Constructs a new UserNotAuthenticatedException with the provided detail message and cause.

android.hardware.GeomagneticField---setRecordingHint:  
Sets recording mode hint. This tells the camera that the intent of the application is to record videos start(), not to take still pictures takePicture(Camera.ShutterCallback, Camera.PictureCallback, Camera.PictureCallback, Camera.PictureCallback). Using this hint can allow MediaRecorder.start() to start faster or with fewer glitches on output. This should be called before starting preview for the best result, but can be changed while the preview is active. The default value is false. The app can still call takePicture() when the hint is true or call MediaRecorder.start() when the hint is false. But the performance may be worse.

android.test.UiThreadTest---getLac:  


java.util.logging.MemoryHandler---logp:  
Log a message, specifying source class and method, with associated Throwable information. If the logger is currently enabled for the given message level then the given arguments are stored in a LogRecord which is forwarded to all registered output handlers. Note that the thrown argument is stored in the LogRecord thrown property, rather than the LogRecord parameters property.  Thus it is processed specially by output Formatters and is not treated as a formatting parameter to the LogRecord message property.

android.net.Uri.Builder---SSLSessionCache:  
Create a session cache at the default location for this app. Multiple instances share data internally.

android.util.MonthDisplayHelper---e:  
Send an ERROR log message.

java.security.Identity---setMessageDigest:  
Associates the specified message digest with this stream.   See also: getMessageDigest()

java.sql.Clob---InvalidKeySpecException:  
Creates a InvalidKeySpecException with the specified cause and a detail message of (cause==null ? null : cause.toString()) (which typically contains the class and detail message of cause).

java.util.logging.MemoryHandler---logp:  
Log a message, specifying source class and method, with an array of object arguments. If the logger is currently enabled for the given message level then a corresponding LogRecord is created and forwarded to all the registered output Handler objects.

java.security.PrivilegedActionException---KeyManagementException:  
Creates a KeyManagementException with the specified cause and a detail message of (cause==null ? null : cause.toString()) (which typically contains the class and detail message of cause).

android.telecom.ConnectionRequest---sendConnectionEvent:  
Sends an event associated with this Connection with associated event extras to the InCallService. Connection events are used to communicate point in time information from a ConnectionService to a InCallService implementations.  An example of a custom connection event includes notifying the UI when a WIFI call has been handed over to LTE, which the InCall UI might use to inform the user that billing charges may apply.  The Android Telephony framework will send the EVENT_CALL_MERGE_FAILED connection event when a call to mergeConference() has failed to complete successfully.  A connection event could also be used to trigger UI in the InCallService which prompts the user to make a choice (e.g. whether they want to incur roaming costs for making a call), which is communicated back via sendCallEvent(String, Bundle). Events are exposed to InCallService implementations via onConnectionEvent(Call, String, Bundle). No assumptions should be made as to how an In-Call UI or service will handle these events. The ConnectionService must assume that the In-Call UI could even chose to ignore some events altogether. Events should be fully qualified (e.g. com.example.event.MY_EVENT) to avoid conflicts between ConnectionService implementations.  Further, custom ConnectionService implementations shall not re-purpose events in the android.* namespace, nor shall they define new event types in this namespace.  When defining a custom event type, ensure the contents of the extras Bundle is clearly defined.  Extra keys for this bundle should be named similar to the event type (e.g. com.example.extra.MY_EXTRA). When defining events and the associated extras, it is important to keep their behavior consistent when the associated ConnectionService is updated.  Support for deprecated events/extras should me maintained to ensure backwards compatibility with older InCallService implementations which were built to support the older behavior.

java.time.chrono.ChronoPeriod---DateTimeException:  
Constructs a new date-time exception with the specified message.

android.bluetooth.BluetoothGattServer---onCharacteristicRead:  
Callback reporting the result of a characteristic read operation.

android.renderscript.Script---loadOrtho:  
Set current values to be an orthographic projection matrix

android.media.MediaDrm.SecurityLevel---requestSingleUpdate:  
Register for a single location update using a Criteria and a callback. See requestLocationUpdates(long, float, Criteria, PendingIntent) for more detail on how to use this method. Requires the ACCESS_COARSE_LOCATION or ACCESS_FINE_LOCATION permissions.

java.util.concurrent.atomic.DoubleAdder---accumulateAndGet:  
Atomically updates the field of the given object managed by this updater with the results of applying the given function to the current and given values, returning the updated value. The function should be side-effect-free, since it may be re-applied when attempted updates fail due to contention among threads.  The function is applied with the current value as its first argument, and the given update as the second argument.

android.telecom.PhoneAccount.Builder---setMuted:  
Sets the microphone mute state. When this request is honored, there will be change to the getCallAudioState().

android.app.NotificationChannel---Notification.MessagingStyle.Message:  
Constructor

android.bluetooth.BluetoothHeadset---notifyCharacteristicChanged:  
Send a notification or indication that a local characteristic has been updated. A notification or indication is sent to the remote device to signal that the characteristic has been updated. This function should be invoked for every client that requests notifications/indications by writing to the "Client Configuration" descriptor for the given characteristic. Requires BLUETOOTH permission.

java.security.interfaces.DSAKey---CertPathValidatorException:  
Creates a CertPathValidatorException that wraps the specified throwable. This allows any exception to be converted into a CertPathValidatorException, while retaining information about the wrapped exception, which may be useful for debugging. The detail message is set to (cause==null ? null : cause.toString()) (which typically contains the class and detail message of cause).

java.security.InvalidParameterException---AccessControlException:  
Constructs an AccessControlException with the specified, detailed message.

android.renderscript.ScriptIntrinsicConvolve5x5---forEachSrcIn:  
Sets dst = src * dst.a

java.lang.FunctionalInterface---UTFDataFormatException:  
Constructs a UTFDataFormatException with null as its error detail message.

android.telephony.mbms.DownloadStateCallback---isEmail:  
This method was deprecated      in API level 4.    Use android.telephony.SmsMessage.  Returns true if message is an email.

java.io.ObjectOutputStream.PutField---resolveProxyClass:  
Returns a proxy class that implements the interfaces named in a proxy class descriptor; subclasses may implement this method to read custom data from the stream along with the descriptors for dynamic proxy classes, allowing them to use an alternate loading mechanism for the interfaces and the proxy class. This method is called exactly once for each unique proxy class descriptor in the stream. The corresponding method in ObjectOutputStream is annotateProxyClass.  For a given subclass of ObjectInputStream that overrides this method, the annotateProxyClass method in the corresponding subclass of ObjectOutputStream must write any data or objects read by this method. The default implementation of this method in ObjectInputStream returns the result of calling Proxy.getProxyClass with the list of Class objects for the interfaces that are named in the interfaces parameter.  The Class object for each interface name i is the value returned by calling Class.forName(i, false, loader) where loader is that of the first non- null class loader up the execution stack, or null if no non- null class loaders are on the stack (the same class loader choice used by the resolveClass method).  Unless any of the resolved interfaces are non-public, this same value of loader is also the class loader passed to Proxy.getProxyClass ; if non-public interfaces are present, their class loader is passed instead (if more than one non-public interface class loader is encountered, an IllegalAccessError is thrown). If Proxy.getProxyClass throws an IllegalArgumentException , resolveProxyClass will throw a ClassNotFoundException containing the IllegalArgumentException .    See also: annotateProxyClass(Class)

android.graphics.BitmapShader---getByteCount:  
Returns the minimum number of bytes that can be used to store this bitmap's pixels. As of KITKAT, the result of this method can no longer be used to determine memory usage of a bitmap. See getAllocationByteCount().

android.hardware.camera2.CameraMetadata---setTorchMode:  
Set the flash unit's torch mode of the camera of the given ID without opening the camera device. Use getCameraIdList() to get the list of available camera devices and use getCameraCharacteristics(String) to check whether the camera device has a flash unit. Note that even if a camera device has a flash unit, turning on the torch mode may fail if the camera device or other camera resources needed to turn on the torch mode are in use.  If setTorchMode(String, boolean) is called to turn on or off the torch mode successfully, onTorchModeChanged(String, boolean) will be invoked. However, even if turning on the torch mode is successful, the application does not have the exclusive ownership of the flash unit or the camera device. The torch mode will be turned off and becomes unavailable when the camera device that the flash unit belongs to becomes unavailable or when other camera resources to keep the torch on become unavailable ( onTorchModeUnavailable(String) will be invoked). Also, other applications are free to call setTorchMode(String, boolean) to turn off the torch mode ( onTorchModeChanged(String, boolean) will be invoked). If the latest application that turned on the torch mode exits, the torch mode will be turned off.

android.media.AudioManager.OnAudioFocusChangeListener---getAccuracy:  
Returns a constant describing horizontal accuracy of this provider. If the provider returns finer grain or exact location, ACCURACY_FINE is returned, otherwise if the location is only approximate then ACCURACY_COARSE is returned.

java.lang.IllegalAccessException---CloneNotSupportedException:  
Constructs a CloneNotSupportedException with no detail message.

android.bluetooth.BluetoothHidDeviceCallback---BluetoothHidDeviceAppQosSettings:  
Create a BluetoothHidDeviceAppQosSettings object for the Bluetooth L2CAP channel. The QoS Settings is optional. Please refer to Bluetooth HID Specfication v1.1.1 Section 5.2 and Appendix D for parameters.

java.security.KeyException---GeneralSecurityException:  
Creates a GeneralSecurityException with the specified cause and a detail message of (cause==null ? null : cause.toString()) (which typically contains the class and detail message of cause).

android.view.ViewDebug---onProvideShadowMetrics:  
Provides the metrics for the shadow image. These include the dimensions of the shadow image, and the point within that shadow that should be centered under the touch location while dragging. The default implementation sets the dimensions of the shadow to be the same as the dimensions of the View itself and centers the shadow under the touch point.

java.lang.NoSuchMethodError---InternalError:  
Constructs an InternalError with no detail message.

java.util.concurrent.ThreadPoolExecutor.AbortPolicy---getQueueLength:  
Returns an estimate of the number of threads waiting to acquire. The value is only an estimate because the number of threads may change dynamically while this method traverses internal data structures.  This method is designed for use in monitoring system state, not for synchronization control.

android.media.MediaDrm.HdcpLevel---Location:  
Construct a new Location object that is copied from an existing one.

android.media.AudioRecord.OnRecordPositionUpdateListener---SettingInjectorService:  
Constructor.

android.os.MessageQueue.IdleHandler---handleMessage:  


java.lang.TypeNotPresentException---ReflectiveOperationException:  
Constructs a new exception with the specified detail message. The cause is not initialized, and may subsequently be initialized by a call to initCause(Throwable).

android.hardware.camera2.CameraMetadata---unregisterTorchCallback:  
Remove a previously-added callback; the callback will no longer receive torch mode status callbacks. Removing a callback that isn't registered has no effect.

android.net.wifi.WpsInfo---setReferenceCounted:  
Controls whether this is a reference-counted or non-reference-counted WifiLock. Reference-counted WifiLocks keep track of the number of calls to acquire() and release(), and only allow the radio to sleep when every call to acquire() has been balanced with a call to release().  Non-reference-counted WifiLocks lock the radio whenever acquire() is called and it is unlocked, and unlock the radio whenever release() is called and it is locked.

java.util.concurrent.atomic.AtomicReference---floatValue:  
Returns the value of this AtomicLong as a float after a widening primitive conversion.

android.nfc.cardemulation.OffHostApduService---isDefaultServiceForCategory:  
Allows an application to query whether a service is currently the default service to handle a card emulation category. Note that if getSelectionModeForCategory(String) returns SELECTION_MODE_ALWAYS_ASK or SELECTION_MODE_ASK_IF_CONFLICT, this method will always return false. That is because in these selection modes a default can't be set at the category level. For categories where the selection mode is SELECTION_MODE_ALWAYS_ASK or SELECTION_MODE_ASK_IF_CONFLICT, use isDefaultServiceForAid(ComponentName, String) to determine whether a service is the default for a specific AID.

android.media.MediaCas.Session---play:  
Play one of the predefined platform sounds for media actions.  Use this method to play a platform-specific sound for various media actions. The sound playback is done asynchronously, with the same behavior and content as the sounds played by Camera.takePicture, MediaRecorder.start, and MediaRecorder.stop.  With the camera2 API, this method can be used to play standard camera operation sounds with the appropriate system behavior for such sounds.  With the older Camera API, using this method makes it easy to match the default device sounds when recording or capturing data through the preview callbacks, or when implementing custom camera-like features in your application.  If the sound has not been loaded by load(int) before calling play, play will load the sound at the cost of some additional latency before sound playback begins.   See also: takePicture(Camera.ShutterCallback, Camera.PictureCallback, Camera.PictureCallback)MediaRecorderSHUTTER_CLICKFOCUS_COMPLETESTART_VIDEO_RECORDINGSTOP_VIDEO_RECORDING

android.telephony.SubscriptionManager---downloadMultimediaMessage:  
Download an MMS message from carrier by a given location URL

android.telephony.mbms.DownloadRequest---sendMultipartTextMessage:  
This method was deprecated      in API level 4.    Use android.telephony.SmsManager.  Send a multi-part text based SMS.  The callee should have already divided the message into correctly sized parts by calling divideMessage.

java.lang.Short---redirectErrorStream:  
Tells whether this process builder merges standard error and standard output. If this property is true, then any error output generated by subprocesses subsequently started by this object's start() method will be merged with the standard output, so that both can be read using the getInputStream() method.  This makes it easier to correlate error messages with the corresponding output. The initial value is false.

java.util.ServiceLoader---setSeed:  
Sets the seed of this random number generator using a single long seed. The general contract of setSeed is that it alters the state of this random number generator object so as to be in exactly the same state as if it had just been created with the argument seed as a seed. The method setSeed is implemented by class Random by atomically updating the seed to (seed ^ 0x5DEECE66DL) & ((1L << 48) - 1) and clearing the haveNextNextGaussian flag used by nextGaussian() . The implementation of setSeed by class Random happens to use only 48 bits of the given seed. In general, however, an overriding method may use all 64 bits of the long argument as a seed value.

android.app.VoiceInteractor.PickOptionRequest.Option---VoiceInteractor.CompleteVoiceRequest:  
Create a new completed voice interaction request.

android.widget.RadioGroup---assignContactFromPhone:  
Assign a contact based on a phone number. This should only be used when the contact's URI is not available, as an extra query will have to be performed to lookup the URI based on the phone number.

javax.xml.parsers.DocumentBuilderFactory---DatatypeConfigurationException:  
Create a new DatatypeConfigurationException with no specified detail message and cause.

android.inputmethodservice.Keyboard---getMaxWidth:  
Return the maximum width, in pixels, available the input method. Input methods are positioned at the bottom of the screen and, unless running in fullscreen, will generally want to be as short as possible so should compute their height based on their contents.  However, they can stretch as much as needed horizontally.  The function returns to you the maximum amount of space available horizontally, which you can use if needed for UI placement. In many cases this is not needed, you can just rely on the normal view layout mechanisms to position your views within the full horizontal space given to the input method. Note that this value can change dynamically, in particular when the screen orientation changes.

javax.crypto.interfaces.DHPrivateKey---IllegalBlockSizeException:  
Constructs an IllegalBlockSizeException with the specified detail message.

