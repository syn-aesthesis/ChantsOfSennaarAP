using System.Collections.Generic;
using System.Linq;
using BepInEx;
using UnityEngine;

namespace ChantsOfSennaarAP;

// based on ArchipelagoBepInExPluginTemplate https://github.com/alwaysintreble/ArchipelagoBepInExPluginTemplate/
public static class ArchipelagoConsole {
    public static bool Hidden = true;

    private static List<string> _logLines = new();
    private static Vector2 _scrollView;
    private static Rect _window;
    private static Rect _scroll;
    private static Rect _text;
    private static Rect _hideShowButton;

    private static GUIStyle _textStyle = new();
    private static string _scrollText = "";
    private static float _lastUpdateTime = Time.time;
    private const int MaxLogLines = 80;
    private const float HideTimeout = 15f;

    private static string _commandText = "!help";
    private static Rect _commandTextRect;
    private static Rect _sendCommandButton;
    
    public static void Awake() {
        UpdateWindow();
    }

    public static void LogMessage(string message) {
        if (message.IsNullOrWhiteSpace())
            return;

        if (_logLines.Count == MaxLogLines) {
            _logLines.RemoveAt(0);
        }

        _logLines.Add(message);
        Plugin.Logger.LogMessage(message);
        _lastUpdateTime = Time.time;
        UpdateWindow();
    }

    public static void OnGUI() {
        if (_logLines.Count == 0)
            return;

        if (!Hidden || Time.time - _lastUpdateTime < HideTimeout) {
            _scrollView = GUI.BeginScrollView(_window, _scrollView, _scroll);
            GUI.Box(_text, "");
            GUI.Box(_text, _scrollText, _textStyle);
            GUI.EndScrollView();
        }

        if (GUI.Button(_hideShowButton, Hidden ? "Show" : "Hide")) {
            Hidden = !Hidden;
            UpdateWindow();
        }

        if (Hidden || !ArchipelagoClient.Authenticated) return;

        _commandText = GUI.TextField(_commandTextRect, _commandText);
        if (!_commandText.IsNullOrWhiteSpace() && GUI.Button(_sendCommandButton, "Send")) {
            Plugin.APClient.SendMessage(_commandText);
            _commandText = "";
        }
    }

    public static void UpdateWindow() {
        _scrollText = "";

        if (Hidden) {
            if (_logLines.Count > 0) {
                _scrollText = _logLines[_logLines.Count - 1];
            }
        }
        else {
            for (int i = 0; i < _logLines.Count; i++) {
                _scrollText += "> ";
                _scrollText += _logLines.ElementAt(i);
                if (i < _logLines.Count - 1) {
                    _scrollText += "\n\n";
                }
            }
        }

        int width = (int)(Screen.width*0.4f);
        int height;
        int scrollDepth;
        if (Hidden) {
            height = (int)(Screen.height*0.03f);
            scrollDepth = height;
        }
        else {
            height = (int)(Screen.height*0.3f);
            scrollDepth = height*10;
        }

        _window = new Rect(Screen.width/2 - width/2, 0, width, height);
        _scroll = new Rect(0, 0, width*0.9f, scrollDepth);
        _scrollView = new Vector2(0, scrollDepth);
        _text = new Rect(0, 0, width, scrollDepth);

        _textStyle.alignment = TextAnchor.LowerLeft;
        _textStyle.fontSize = Hidden ? (int)(Screen.height*0.0165f) : (int)(Screen.height*0.0185f);
        _textStyle.normal.textColor = Color.white;
        _textStyle.wordWrap = !Hidden;
        
        var xPadding = (int)(Screen.width*0.01f);
        var yPadding = (int)(Screen.height*0.01f);

        _textStyle.padding = Hidden
            ? new RectOffset(xPadding/2, xPadding/2, yPadding/2, yPadding/2)
            : new RectOffset(xPadding, xPadding, yPadding, yPadding);

        var buttonWidth = (int)(Screen.width*0.12f);
        var buttonHeight = (int)(Screen.height*0.03f);

        _hideShowButton = new Rect(Screen.width/2 + width/2 + buttonWidth/3, Screen.height * 0.004f, buttonWidth,
            buttonHeight);

        width = (int)(Screen.width * 0.4f);
        var xPos = (int)(Screen.width*0.5f - width*0.5f);
        var yPos = (int)(Screen.height*0.307f);
        height = (int)(Screen.height*0.022f);

        _commandTextRect = new Rect(xPos, yPos, width, height);
        
        width = (int)(Screen.width*0.035f);
        yPos += (int)(Screen.height*0.03f);
        _sendCommandButton = new Rect(xPos, yPos, width, height);
    }
}