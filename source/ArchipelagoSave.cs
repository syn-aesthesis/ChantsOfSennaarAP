using System;
using System.Collections.Generic;
using System.IO;
using BepInEx;
using UnityEngine;

namespace ChantsOfSennaarAP;

[Serializable]
public class ArchipelagoSave {
    public string Seed;
    public string SlotName;
    public int Team;

    public List<string> CheckedLocationNames = new();
    public bool GoalReached;

    private static readonly object Lock = new();

    public static ArchipelagoSave LoadOrCreate(string seed, string slot, int team) {
        var path = PathFor(seed, slot, team);
        try {
            if (File.Exists(path))
                return JsonUtility.FromJson<ArchipelagoSave>(File.ReadAllText(path));
        }
        catch (Exception e) {
            Plugin.Logger.LogError($"AP save load failed: {e}");
        }

        return new ArchipelagoSave { Seed = seed, SlotName = slot, Team = team };
    }
    
    public bool AddCheck(string name) {
        lock (Lock) {
            if (CheckedLocationNames.Contains(name))
                return false;
            CheckedLocationNames.Add(name);
            return true;
        }
    }

    public string[] SnapshotChecks() {
        lock (Lock) {
            return CheckedLocationNames.ToArray();
        }
    }

    public void Save() {
        lock (Lock) {
            var path = PathFor(Seed, SlotName, Team);
            var tmp = path + ".tmp";

            try {
                Directory.CreateDirectory(SaveDir);
                File.WriteAllText(tmp, JsonUtility.ToJson(this, true));

                if (File.Exists(path))
                    File.Replace(tmp, path, null);
                else
                    File.Move(tmp, path);
            }
            catch (Exception e) {
                Plugin.Logger.LogError($"AP save write failed: {e}");
            }
        }
    }

    private static string SaveDir => Path.Combine(Paths.ConfigPath, Plugin.PluginName);

    private static string PathFor(string seed, string slot, int team) =>
        Path.Combine(SaveDir, $"{Sanitize(seed)}_{team}_{Sanitize(slot)}.json");

    private static string Sanitize(string s) =>
        string.Concat(s.Split(Path.GetInvalidFileNameChars()));
}