using System.Collections.Generic;
using Newtonsoft.Json;

namespace ChantsOfSennaarAP;

// based on ArchipelagoBepInExPluginTemplate https://github.com/alwaysintreble/ArchipelagoBepInExPluginTemplate/
public class ArchipelagoData {
    public string Server;
    public string Slot;
    public string Password;

    public int Index;
    public List<long> CheckedLocations;
    private string _seed;
    private Dictionary<string, object> _slotData;
    public bool NeedSlotData => _slotData == null;

    public ArchipelagoData() {
        Server = "localhost";
        Slot = "Player1";
        CheckedLocations = new();
    }

    public ArchipelagoData(string server, string slot, string password) {
        Server = server;
        Slot = slot;
        Password = password;
        CheckedLocations = new();
    }

    public void SetupSession(Dictionary<string, object> roomSlotData, string roomSeed) {
        _slotData = roomSlotData;
        _seed = roomSeed;
    }

    public override string ToString() {
        return JsonConvert.SerializeObject(this);
    }
}