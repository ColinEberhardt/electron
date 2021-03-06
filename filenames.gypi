{
  'variables': {
    'app_sources': [
      'atom/app/atom_main.cc',
      'atom/app/atom_main.h',
    ],
    'bundle_sources': [
      'atom/browser/resources/mac/electron.icns',
    ],
    'js_sources': [
      'lib/browser/api/app.js',
      'lib/browser/api/auto-updater.js',
      'lib/browser/api/auto-updater/auto-updater-native.js',
      'lib/browser/api/auto-updater/auto-updater-win.js',
      'lib/browser/api/auto-updater/squirrel-update-win.js',
      'lib/browser/api/browser-window.js',
      'lib/browser/api/content-tracing.js',
      'lib/browser/api/dialog.js',
      'lib/browser/api/exports/electron.js',
      'lib/browser/api/global-shortcut.js',
      'lib/browser/api/ipc-main.js',
      'lib/browser/api/menu.js',
      'lib/browser/api/menu-item.js',
      'lib/browser/api/navigation-controller.js',
      'lib/browser/api/power-monitor.js',
      'lib/browser/api/power-save-blocker.js',
      'lib/browser/api/protocol.js',
      'lib/browser/api/session.js',
      'lib/browser/api/screen.js',
      'lib/browser/api/system-preferences.js',
      'lib/browser/api/tray.js',
      'lib/browser/api/web-contents.js',
      'lib/browser/chrome-extension.js',
      'lib/browser/desktop-capturer.js',
      'lib/browser/guest-view-manager.js',
      'lib/browser/guest-window-manager.js',
      'lib/browser/init.js',
      'lib/browser/objects-registry.js',
      'lib/browser/rpc-server.js',
      'lib/common/api/callbacks-registry.js',
      'lib/common/api/clipboard.js',
      'lib/common/api/crash-reporter.js',
      'lib/common/api/deprecate.js',
      'lib/common/api/deprecations.js',
      'lib/common/api/is-promise.js',
      'lib/common/api/exports/electron.js',
      'lib/common/api/native-image.js',
      'lib/common/api/shell.js',
      'lib/common/init.js',
      'lib/common/reset-search-paths.js',
      'lib/renderer/chrome-api.js',
      'lib/renderer/content-scripts-injector.js',
      'lib/renderer/init.js',
      'lib/renderer/inspector.js',
      'lib/renderer/override.js',
      'lib/renderer/web-view/guest-view-internal.js',
      'lib/renderer/web-view/web-view.js',
      'lib/renderer/web-view/web-view-attributes.js',
      'lib/renderer/web-view/web-view-constants.js',
      'lib/renderer/api/desktop-capturer.js',
      'lib/renderer/api/exports/electron.js',
      'lib/renderer/api/ipc-renderer.js',
      'lib/renderer/api/remote.js',
      'lib/renderer/api/screen.js',
      'lib/renderer/api/web-frame.js',
    ],
    'js2c_sources': [
      'lib/common/asar.js',
      'lib/common/asar_init.js',
    ],
    'default_app_sources': [
      'default_app/default_app.js',
      'default_app/index.html',
      'default_app/main.js',
      'default_app/package.json',
    ],
    'lib_sources': [
      'atom/app/atom_content_client.cc',
      'atom/app/atom_content_client.h',
      'atom/app/atom_main_delegate.cc',
      'atom/app/atom_main_delegate.h',
      'atom/app/atom_main_delegate_mac.mm',
      'atom/app/node_main.cc',
      'atom/app/node_main.h',
      'atom/app/uv_task_runner.cc',
      'atom/app/uv_task_runner.h',
      'atom/browser/api/atom_api_app.cc',
      'atom/browser/api/atom_api_app.h',
      'atom/browser/api/atom_api_auto_updater.cc',
      'atom/browser/api/atom_api_auto_updater.h',
      'atom/browser/api/atom_api_content_tracing.cc',
      'atom/browser/api/atom_api_cookies.cc',
      'atom/browser/api/atom_api_cookies.h',
      'atom/browser/api/atom_api_debugger.cc',
      'atom/browser/api/atom_api_debugger.h',
      'atom/browser/api/atom_api_desktop_capturer.cc',
      'atom/browser/api/atom_api_desktop_capturer.h',
      'atom/browser/api/atom_api_download_item.cc',
      'atom/browser/api/atom_api_download_item.h',
      'atom/browser/api/atom_api_dialog.cc',
      'atom/browser/api/atom_api_global_shortcut.cc',
      'atom/browser/api/atom_api_global_shortcut.h',
      'atom/browser/api/atom_api_menu.cc',
      'atom/browser/api/atom_api_menu.h',
      'atom/browser/api/atom_api_menu_views.cc',
      'atom/browser/api/atom_api_menu_views.h',
      'atom/browser/api/atom_api_menu_mac.h',
      'atom/browser/api/atom_api_menu_mac.mm',
      'atom/browser/api/atom_api_power_monitor.cc',
      'atom/browser/api/atom_api_power_monitor.h',
      'atom/browser/api/atom_api_power_save_blocker.cc',
      'atom/browser/api/atom_api_power_save_blocker.h',
      'atom/browser/api/atom_api_render_process_preferences.cc',
      'atom/browser/api/atom_api_render_process_preferences.h',
      'atom/browser/api/atom_api_protocol.cc',
      'atom/browser/api/atom_api_protocol.h',
      'atom/browser/api/atom_api_screen.cc',
      'atom/browser/api/atom_api_screen.h',
      'atom/browser/api/atom_api_session.cc',
      'atom/browser/api/atom_api_session.h',
      'atom/browser/api/atom_api_system_preferences.cc',
      'atom/browser/api/atom_api_system_preferences.h',
      'atom/browser/api/atom_api_system_preferences_mac.mm',
      'atom/browser/api/atom_api_tray.cc',
      'atom/browser/api/atom_api_tray.h',
      'atom/browser/api/atom_api_web_contents.cc',
      'atom/browser/api/atom_api_web_contents.h',
      'atom/browser/api/atom_api_web_request.cc',
      'atom/browser/api/atom_api_web_request.h',
      'atom/browser/api/atom_api_web_view_manager.cc',
      'atom/browser/api/atom_api_window.cc',
      'atom/browser/api/atom_api_window.h',
      'atom/browser/api/event.cc',
      'atom/browser/api/event.h',
      'atom/browser/api/event_emitter.cc',
      'atom/browser/api/event_emitter.h',
      'atom/browser/api/trackable_object.cc',
      'atom/browser/api/trackable_object.h',
      'atom/browser/api/frame_subscriber.cc',
      'atom/browser/api/frame_subscriber.h',
      'atom/browser/api/save_page_handler.cc',
      'atom/browser/api/save_page_handler.h',
      'atom/browser/auto_updater.cc',
      'atom/browser/auto_updater.h',
      'atom/browser/auto_updater_mac.mm',
      'atom/browser/atom_access_token_store.cc',
      'atom/browser/atom_access_token_store.h',
      'atom/browser/atom_browser_client.cc',
      'atom/browser/atom_browser_client.h',
      'atom/browser/atom_browser_context.cc',
      'atom/browser/atom_browser_context.h',
      'atom/browser/atom_download_manager_delegate.cc',
      'atom/browser/atom_download_manager_delegate.h',
      'atom/browser/atom_browser_main_parts.cc',
      'atom/browser/atom_browser_main_parts.h',
      'atom/browser/atom_browser_main_parts_mac.mm',
      'atom/browser/atom_browser_main_parts_posix.cc',
      'atom/browser/atom_javascript_dialog_manager.cc',
      'atom/browser/atom_javascript_dialog_manager.h',
      'atom/browser/atom_permission_manager.cc',
      'atom/browser/atom_permission_manager.h',
      'atom/browser/atom_quota_permission_context.cc',
      'atom/browser/atom_quota_permission_context.h',
      'atom/browser/atom_resource_dispatcher_host_delegate.cc',
      'atom/browser/atom_resource_dispatcher_host_delegate.h',
      'atom/browser/atom_security_state_model_client.cc',
      'atom/browser/atom_security_state_model_client.h',
      'atom/browser/atom_speech_recognition_manager_delegate.cc',
      'atom/browser/atom_speech_recognition_manager_delegate.h',
      'atom/browser/bridge_task_runner.cc',
      'atom/browser/bridge_task_runner.h',
      'atom/browser/browser.cc',
      'atom/browser/browser.h',
      'atom/browser/browser_linux.cc',
      'atom/browser/browser_mac.mm',
      'atom/browser/browser_win.cc',
      'atom/browser/browser_observer.h',
      'atom/browser/common_web_contents_delegate_mac.mm',
      'atom/browser/common_web_contents_delegate_views.cc',
      'atom/browser/common_web_contents_delegate.cc',
      'atom/browser/common_web_contents_delegate.h',
      'atom/browser/javascript_environment.cc',
      'atom/browser/javascript_environment.h',
      'atom/browser/login_handler.cc',
      'atom/browser/login_handler.h',
      'atom/browser/mac/atom_application.h',
      'atom/browser/mac/atom_application.mm',
      'atom/browser/mac/atom_application_delegate.h',
      'atom/browser/mac/atom_application_delegate.mm',
      'atom/browser/mac/dict_util.h',
      'atom/browser/mac/dict_util.mm',
      'atom/browser/native_window.cc',
      'atom/browser/native_window.h',
      'atom/browser/native_window_views_win.cc',
      'atom/browser/native_window_views.cc',
      'atom/browser/native_window_views.h',
      'atom/browser/native_window_mac.h',
      'atom/browser/native_window_mac.mm',
      'atom/browser/native_window_observer.h',
      'atom/browser/net/asar/asar_protocol_handler.cc',
      'atom/browser/net/asar/asar_protocol_handler.h',
      'atom/browser/net/asar/url_request_asar_job.cc',
      'atom/browser/net/asar/url_request_asar_job.h',
      'atom/browser/net/atom_cert_verifier.cc',
      'atom/browser/net/atom_cert_verifier.h',
      'atom/browser/net/atom_network_delegate.cc',
      'atom/browser/net/atom_network_delegate.h',
      'atom/browser/net/atom_ssl_config_service.cc',
      'atom/browser/net/atom_ssl_config_service.h',
      'atom/browser/net/atom_url_request_job_factory.cc',
      'atom/browser/net/atom_url_request_job_factory.h',
      'atom/browser/net/http_protocol_handler.cc',
      'atom/browser/net/http_protocol_handler.h',
      'atom/browser/net/js_asker.cc',
      'atom/browser/net/js_asker.h',
      'atom/browser/net/url_request_async_asar_job.cc',
      'atom/browser/net/url_request_async_asar_job.h',
      'atom/browser/net/url_request_string_job.cc',
      'atom/browser/net/url_request_string_job.h',
      'atom/browser/net/url_request_buffer_job.cc',
      'atom/browser/net/url_request_buffer_job.h',
      'atom/browser/net/url_request_fetch_job.cc',
      'atom/browser/net/url_request_fetch_job.h',
      'atom/browser/node_debugger.cc',
      'atom/browser/node_debugger.h',
      'atom/browser/render_process_preferences.cc',
      'atom/browser/render_process_preferences.h',
      'atom/browser/ui/accelerator_util.cc',
      'atom/browser/ui/accelerator_util.h',
      'atom/browser/ui/accelerator_util_mac.mm',
      'atom/browser/ui/accelerator_util_views.cc',
      'atom/browser/ui/atom_menu_model.cc',
      'atom/browser/ui/atom_menu_model.h',
      'atom/browser/ui/cocoa/atom_menu_controller.h',
      'atom/browser/ui/cocoa/atom_menu_controller.mm',
      'atom/browser/ui/file_dialog.h',
      'atom/browser/ui/file_dialog_gtk.cc',
      'atom/browser/ui/file_dialog_mac.mm',
      'atom/browser/ui/file_dialog_win.cc',
      'atom/browser/ui/message_box.h',
      'atom/browser/ui/message_box_gtk.cc',
      'atom/browser/ui/message_box_mac.mm',
      'atom/browser/ui/message_box_win.cc',
      'atom/browser/ui/tray_icon.cc',
      'atom/browser/ui/tray_icon.h',
      'atom/browser/ui/tray_icon_gtk.cc',
      'atom/browser/ui/tray_icon_gtk.h',
      'atom/browser/ui/tray_icon_cocoa.h',
      'atom/browser/ui/tray_icon_cocoa.mm',
      'atom/browser/ui/tray_icon_observer.h',
      'atom/browser/ui/tray_icon_win.cc',
      'atom/browser/ui/views/frameless_view.cc',
      'atom/browser/ui/views/frameless_view.h',
      'atom/browser/ui/views/global_menu_bar_x11.cc',
      'atom/browser/ui/views/global_menu_bar_x11.h',
      'atom/browser/ui/views/menu_bar.cc',
      'atom/browser/ui/views/menu_bar.h',
      'atom/browser/ui/views/menu_delegate.cc',
      'atom/browser/ui/views/menu_delegate.h',
      'atom/browser/ui/views/menu_layout.cc',
      'atom/browser/ui/views/menu_layout.h',
      'atom/browser/ui/views/native_frame_view.cc',
      'atom/browser/ui/views/native_frame_view.h',
      'atom/browser/ui/views/submenu_button.cc',
      'atom/browser/ui/views/submenu_button.h',
      'atom/browser/ui/views/win_frame_view.cc',
      'atom/browser/ui/views/win_frame_view.h',
      'atom/browser/ui/win/atom_desktop_window_tree_host_win.cc',
      'atom/browser/ui/win/atom_desktop_window_tree_host_win.h',
      'atom/browser/ui/win/message_handler_delegate.cc',
      'atom/browser/ui/win/message_handler_delegate.h',
      'atom/browser/ui/win/notify_icon_host.cc',
      'atom/browser/ui/win/notify_icon_host.h',
      'atom/browser/ui/win/notify_icon.cc',
      'atom/browser/ui/win/notify_icon.h',
      'atom/browser/ui/win/taskbar_host.cc',
      'atom/browser/ui/win/taskbar_host.h',
      'atom/browser/ui/x/window_state_watcher.cc',
      'atom/browser/ui/x/window_state_watcher.h',
      'atom/browser/ui/x/x_window_utils.cc',
      'atom/browser/ui/x/x_window_utils.h',
      'atom/browser/web_contents_permission_helper.cc',
      'atom/browser/web_contents_permission_helper.h',
      'atom/browser/web_contents_preferences.cc',
      'atom/browser/web_contents_preferences.h',
      'atom/browser/web_dialog_helper.cc',
      'atom/browser/web_dialog_helper.h',
      'atom/browser/web_view_guest_delegate.cc',
      'atom/browser/web_view_guest_delegate.h',
      'atom/browser/web_view_manager.cc',
      'atom/browser/web_view_manager.h',
      'atom/browser/window_list.cc',
      'atom/browser/window_list.h',
      'atom/browser/window_list_observer.h',
      'atom/common/api/api_messages.h',
      'atom/common/api/atom_api_asar.cc',
      'atom/common/api/atom_api_clipboard.cc',
      'atom/common/api/atom_api_crash_reporter.cc',
      'atom/common/api/atom_api_key_weak_map.h',
      'atom/common/api/atom_api_native_image.cc',
      'atom/common/api/atom_api_native_image.h',
      'atom/common/api/atom_api_native_image_mac.mm',
      'atom/common/api/atom_api_shell.cc',
      'atom/common/api/atom_api_v8_util.cc',
      'atom/common/api/atom_bindings.cc',
      'atom/common/api/atom_bindings.h',
      'atom/common/api/event_emitter_caller.cc',
      'atom/common/api/event_emitter_caller.h',
      'atom/common/api/locker.cc',
      'atom/common/api/locker.h',
      'atom/common/api/object_life_monitor.cc',
      'atom/common/api/object_life_monitor.h',
      'atom/common/api/remote_callback_freer.cc',
      'atom/common/api/remote_callback_freer.h',
      'atom/common/api/remote_object_freer.cc',
      'atom/common/api/remote_object_freer.h',
      'atom/common/asar/archive.cc',
      'atom/common/asar/archive.h',
      'atom/common/asar/asar_util.cc',
      'atom/common/asar/asar_util.h',
      'atom/common/asar/scoped_temporary_file.cc',
      'atom/common/asar/scoped_temporary_file.h',
      'atom/common/atom_command_line.cc',
      'atom/common/atom_command_line.h',
      'atom/common/atom_constants.cc',
      'atom/common/atom_constants.h',
      'atom/common/color_util.cc',
      'atom/common/color_util.h',
      'atom/common/common_message_generator.cc',
      'atom/common/common_message_generator.h',
      'atom/common/crash_reporter/crash_reporter.cc',
      'atom/common/crash_reporter/crash_reporter.h',
      'atom/common/crash_reporter/crash_reporter_linux.cc',
      'atom/common/crash_reporter/crash_reporter_linux.h',
      'atom/common/crash_reporter/crash_reporter_mac.h',
      'atom/common/crash_reporter/crash_reporter_mac.mm',
      'atom/common/crash_reporter/crash_reporter_win.cc',
      'atom/common/crash_reporter/crash_reporter_win.h',
      'atom/common/crash_reporter/linux/crash_dump_handler.cc',
      'atom/common/crash_reporter/linux/crash_dump_handler.h',
      'atom/common/crash_reporter/win/crash_service.cc',
      'atom/common/crash_reporter/win/crash_service.h',
      'atom/common/crash_reporter/win/crash_service_main.cc',
      'atom/common/crash_reporter/win/crash_service_main.h',
      'atom/common/draggable_region.cc',
      'atom/common/draggable_region.h',
      'atom/common/google_api_key.h',
      'atom/common/key_weak_map.h',
      'atom/common/keyboard_util.cc',
      'atom/common/keyboard_util.h',
      'atom/common/mouse_util.cc',
      'atom/common/mouse_util.h',
      'atom/common/linux/application_info.cc',
      'atom/common/native_mate_converters/accelerator_converter.cc',
      'atom/common/native_mate_converters/accelerator_converter.h',
      'atom/common/native_mate_converters/blink_converter.cc',
      'atom/common/native_mate_converters/blink_converter.h',
      'atom/common/native_mate_converters/callback.cc',
      'atom/common/native_mate_converters/callback.h',
      'atom/common/native_mate_converters/content_converter.cc',
      'atom/common/native_mate_converters/content_converter.h',
      'atom/common/native_mate_converters/file_path_converter.h',
      'atom/common/native_mate_converters/gfx_converter.cc',
      'atom/common/native_mate_converters/gfx_converter.h',
      'atom/common/native_mate_converters/gurl_converter.h',
      'atom/common/native_mate_converters/image_converter.cc',
      'atom/common/native_mate_converters/image_converter.h',
      'atom/common/native_mate_converters/net_converter.cc',
      'atom/common/native_mate_converters/net_converter.h',
      'atom/common/native_mate_converters/string16_converter.h',
      'atom/common/native_mate_converters/ui_base_types_converter.h',
      'atom/common/native_mate_converters/v8_value_converter.cc',
      'atom/common/native_mate_converters/v8_value_converter.h',
      'atom/common/native_mate_converters/value_converter.cc',
      'atom/common/native_mate_converters/value_converter.h',
      'atom/common/node_bindings.cc',
      'atom/common/node_bindings.h',
      'atom/common/node_bindings_linux.cc',
      'atom/common/node_bindings_linux.h',
      'atom/common/node_bindings_mac.cc',
      'atom/common/node_bindings_mac.h',
      'atom/common/node_bindings_win.cc',
      'atom/common/node_bindings_win.h',
      'atom/common/node_includes.h',
      'atom/common/options_switches.cc',
      'atom/common/options_switches.h',
      'atom/common/platform_util.h',
      'atom/common/platform_util_linux.cc',
      'atom/common/platform_util_mac.mm',
      'atom/common/platform_util_win.cc',
      'atom/renderer/api/atom_api_renderer_ipc.cc',
      'atom/renderer/api/atom_api_spell_check_client.cc',
      'atom/renderer/api/atom_api_spell_check_client.h',
      'atom/renderer/api/atom_api_web_frame.cc',
      'atom/renderer/api/atom_api_web_frame.h',
      'atom/renderer/atom_render_view_observer.cc',
      'atom/renderer/atom_render_view_observer.h',
      'atom/renderer/atom_renderer_client.cc',
      'atom/renderer/atom_renderer_client.h',
      'atom/renderer/guest_view_container.cc',
      'atom/renderer/guest_view_container.h',
      'atom/renderer/node_array_buffer_bridge.cc',
      'atom/renderer/node_array_buffer_bridge.h',
      'atom/renderer/preferences_manager.cc',
      'atom/renderer/preferences_manager.h',
      'atom/utility/atom_content_utility_client.cc',
      'atom/utility/atom_content_utility_client.h',
      'chromium_src/chrome/browser/browser_process.cc',
      'chromium_src/chrome/browser/browser_process.h',
      'chromium_src/chrome/browser/chrome_process_finder_win.cc',
      'chromium_src/chrome/browser/chrome_process_finder_win.h',
      'chromium_src/chrome/browser/chrome_notification_types.h',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener.cc',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener.h',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener_mac.mm',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener_mac.h',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener_x11.cc',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener_x11.h',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener_win.cc',
      'chromium_src/chrome/browser/extensions/global_shortcut_listener_win.h',
      'chromium_src/chrome/browser/media/desktop_media_list.h',
      'chromium_src/chrome/browser/media/desktop_media_list_observer.h',
      'chromium_src/chrome/browser/media/native_desktop_media_list.cc',
      'chromium_src/chrome/browser/media/native_desktop_media_list.h',
      'chromium_src/chrome/browser/printing/print_job.cc',
      'chromium_src/chrome/browser/printing/print_job.h',
      'chromium_src/chrome/browser/printing/print_job_manager.cc',
      'chromium_src/chrome/browser/printing/print_job_manager.h',
      'chromium_src/chrome/browser/printing/print_job_worker.cc',
      'chromium_src/chrome/browser/printing/print_job_worker.h',
      'chromium_src/chrome/browser/printing/print_job_worker_owner.cc',
      'chromium_src/chrome/browser/printing/print_job_worker_owner.h',
      'chromium_src/chrome/browser/printing/print_view_manager_base.cc',
      'chromium_src/chrome/browser/printing/print_view_manager_base.h',
      'chromium_src/chrome/browser/printing/print_view_manager_basic.cc',
      'chromium_src/chrome/browser/printing/print_view_manager_basic.h',
      'chromium_src/chrome/browser/printing/print_view_manager_observer.h',
      'chromium_src/chrome/browser/printing/printer_query.cc',
      'chromium_src/chrome/browser/printing/printer_query.h',
      'chromium_src/chrome/browser/printing/printing_message_filter.cc',
      'chromium_src/chrome/browser/printing/printing_message_filter.h',
      'chromium_src/chrome/browser/printing/print_preview_message_handler.cc',
      'chromium_src/chrome/browser/printing/print_preview_message_handler.h',
      'chromium_src/chrome/browser/process_singleton_posix.cc',
      'chromium_src/chrome/browser/process_singleton_win.cc',
      'chromium_src/chrome/browser/process_singleton.h',
      'chromium_src/chrome/browser/renderer_host/pepper/chrome_browser_pepper_host_factory.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/chrome_browser_pepper_host_factory.h',
      'chromium_src/chrome/browser/renderer_host/pepper/monitor_finder_mac.h',
      'chromium_src/chrome/browser/renderer_host/pepper/monitor_finder_mac.mm',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_broker_message_filter.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_broker_message_filter.h',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_flash_browser_host.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_flash_browser_host.h',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_flash_clipboard_message_filter.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_flash_clipboard_message_filter.h',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_flash_drm_host.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_flash_drm_host.h',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_isolated_file_system_message_filter.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/pepper_isolated_file_system_message_filter.h',
      'chromium_src/chrome/browser/renderer_host/pepper/widevine_cdm_message_filter.cc',
      'chromium_src/chrome/browser/renderer_host/pepper/widevine_cdm_message_filter.h',
      'chromium_src/chrome/browser/speech/tts_controller.h',
      'chromium_src/chrome/browser/speech/tts_controller_impl.cc',
      'chromium_src/chrome/browser/speech/tts_controller_impl.h',
      'chromium_src/chrome/browser/speech/tts_linux.cc',
      'chromium_src/chrome/browser/speech/tts_mac.mm',
      'chromium_src/chrome/browser/speech/tts_message_filter.cc',
      'chromium_src/chrome/browser/speech/tts_message_filter.h',
      'chromium_src/chrome/browser/speech/tts_platform.cc',
      'chromium_src/chrome/browser/speech/tts_platform.h',
      'chromium_src/chrome/browser/speech/tts_win.cc',
      'chromium_src/chrome/browser/ui/browser_dialogs.h',
      'chromium_src/chrome/browser/ui/cocoa/color_chooser_mac.mm',
      'chromium_src/chrome/browser/ui/views/color_chooser_aura.cc',
      'chromium_src/chrome/browser/ui/views/color_chooser_aura.h',
      'chromium_src/chrome/browser/ui/views/frame/global_menu_bar_registrar_x11.cc',
      'chromium_src/chrome/browser/ui/views/frame/global_menu_bar_registrar_x11.h',
      'chromium_src/chrome/common/chrome_constants.cc',
      'chromium_src/chrome/common/chrome_constants.h',
      'chromium_src/chrome/common/chrome_paths.cc',
      'chromium_src/chrome/common/chrome_paths.h',
      'chromium_src/chrome/common/chrome_paths_internal.h',
      'chromium_src/chrome/common/chrome_paths_linux.cc',
      'chromium_src/chrome/common/chrome_paths_mac.mm',
      'chromium_src/chrome/common/chrome_paths_win.cc',
      'chromium_src/chrome/common/chrome_utility_messages.h',
      'chromium_src/chrome/common/pref_names.cc',
      'chromium_src/chrome/common/pref_names.h',
      'chromium_src/chrome/common/print_messages.cc',
      'chromium_src/chrome/common/print_messages.h',
      'chromium_src/chrome/common/tts_messages.h',
      'chromium_src/chrome/common/tts_utterance_request.cc',
      'chromium_src/chrome/common/tts_utterance_request.h',
      'chromium_src/chrome/common/widevine_cdm_messages.h',
      'chromium_src/chrome/common/widevine_cdm_constants.cc',
      'chromium_src/chrome/common/widevine_cdm_constants.h',
      'chromium_src/chrome/renderer/media/chrome_key_systems.cc',
      'chromium_src/chrome/renderer/media/chrome_key_systems.h',
      'chromium_src/chrome/renderer/pepper/chrome_renderer_pepper_host_factory.cc',
      'chromium_src/chrome/renderer/pepper/chrome_renderer_pepper_host_factory.h',
      'chromium_src/chrome/renderer/pepper/pepper_flash_font_file_host.cc',
      'chromium_src/chrome/renderer/pepper/pepper_flash_font_file_host.h',
      'chromium_src/chrome/renderer/pepper/pepper_flash_fullscreen_host.cc',
      'chromium_src/chrome/renderer/pepper/pepper_flash_fullscreen_host.h',
      'chromium_src/chrome/renderer/pepper/pepper_flash_menu_host.cc',
      'chromium_src/chrome/renderer/pepper/pepper_flash_menu_host.h',
      'chromium_src/chrome/renderer/pepper/pepper_flash_renderer_host.cc',
      'chromium_src/chrome/renderer/pepper/pepper_flash_renderer_host.h',
      'chromium_src/chrome/renderer/pepper/pepper_helper.cc',
      'chromium_src/chrome/renderer/pepper/pepper_helper.h',
      'chromium_src/chrome/renderer/pepper/pepper_shared_memory_message_filter.cc',
      'chromium_src/chrome/renderer/pepper/pepper_shared_memory_message_filter.h',
      'chromium_src/chrome/renderer/printing/print_web_view_helper.cc',
      'chromium_src/chrome/renderer/printing/print_web_view_helper_linux.cc',
      'chromium_src/chrome/renderer/printing/print_web_view_helper_mac.mm',
      'chromium_src/chrome/renderer/printing/print_web_view_helper_pdf_win.cc',
      'chromium_src/chrome/renderer/printing/print_web_view_helper.h',
      'chromium_src/chrome/renderer/spellchecker/spellcheck_worditerator.cc',
      'chromium_src/chrome/renderer/spellchecker/spellcheck_worditerator.h',
      'chromium_src/chrome/renderer/tts_dispatcher.cc',
      'chromium_src/chrome/renderer/tts_dispatcher.h',
      'chromium_src/chrome/utility/utility_message_handler.h',
      'chromium_src/extensions/browser/app_window/size_constraints.cc',
      'chromium_src/extensions/browser/app_window/size_constraints.h',
      'chromium_src/extensions/common/url_pattern.cc',
      'chromium_src/extensions/common/url_pattern.h',
      'chromium_src/library_loaders/libspeechd_loader.cc',
      'chromium_src/library_loaders/libspeechd.h',
      'chromium_src/net/test/embedded_test_server/stream_listen_socket.cc',
      'chromium_src/net/test/embedded_test_server/stream_listen_socket.h',
      'chromium_src/net/test/embedded_test_server/tcp_listen_socket.cc',
      'chromium_src/net/test/embedded_test_server/tcp_listen_socket.h',
      '<@(native_mate_files)',
      '<(SHARED_INTERMEDIATE_DIR)/atom_natives.h',
    ],
    'lib_sources_nss': [
      'chromium_src/chrome/browser/certificate_manager_model.cc',
      'chromium_src/chrome/browser/certificate_manager_model.h',
    ],
    'lib_sources_win': [
      'chromium_src/chrome/browser/ui/views/color_chooser_dialog.cc',
      'chromium_src/chrome/browser/ui/views/color_chooser_dialog.h',
      'chromium_src/chrome/browser/ui/views/color_chooser_win.cc',
      'chromium_src/chrome/browser/printing/pdf_to_emf_converter.cc',
      'chromium_src/chrome/browser/printing/pdf_to_emf_converter.h',
      'chromium_src/chrome/utility/printing_handler_win.cc',
      'chromium_src/chrome/utility/printing_handler_win.h',
    ],
    'framework_sources': [
      'atom/app/atom_library_main.h',
      'atom/app/atom_library_main.mm',
    ],
    'locales': [
      'am', 'ar', 'bg', 'bn', 'ca', 'cs', 'da', 'de', 'el', 'en-GB',
      'en-US', 'es-419', 'es', 'et', 'fa', 'fi', 'fil', 'fr', 'gu', 'he',
      'hi', 'hr', 'hu', 'id', 'it', 'ja', 'kn', 'ko', 'lt', 'lv',
      'ml', 'mr', 'ms', 'nb', 'nl', 'pl', 'pt-BR', 'pt-PT', 'ro', 'ru',
      'sk', 'sl', 'sr', 'sv', 'sw', 'ta', 'te', 'th', 'tr', 'uk',
      'vi', 'zh-CN', 'zh-TW',
    ],
    'conditions': [
      ['OS=="win"', {
        'app_sources': [
          'atom/browser/resources/win/resource.h',
          'atom/browser/resources/win/atom.ico',
          'atom/browser/resources/win/atom.rc',
          # Cursors.
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/aliasb.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/cell.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/col_resize.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/copy.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/hand_grab.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/hand_grabbing.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/none.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/pan_east.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/pan_middle.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/pan_north.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/pan_north_east.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/pan_north_west.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/pan_south.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/pan_south_east.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/pan_south_west.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/pan_west.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/row_resize.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/vertical_text.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/zoom_in.cur',
          '<(libchromiumcontent_src_dir)/ui/resources/cursors/zoom_out.cur',
        ],
      }],  # OS=="win"
    ],
  },
}
