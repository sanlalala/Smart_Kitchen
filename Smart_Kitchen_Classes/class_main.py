import class_kitchen
import Smart_Kitchen_Classes.LSL_Integration.lsl_broadcaster as lsl
import time

# import http.server
# import socketserver
import queue

if __name__ == '__main__':
    event_queue = queue.Queue()
    event_broadcaster = lsl.LslEventBroadcaster(event_queue)

    while True:
        event_queue.put(["Schrank1", "Topf1", "take out"])
        time.sleep(3)

    #event_broadcaster.send_event_to_lslStream(["Schrank1", "Topf1", "take out"])
    # Initalisieren der Küche:
    # myKitchen = class_kitchen.Kitchen("My Kitchen")
    # myKitchen.initialize_kitchen_from_config(myKitchen)

    # Man bekommt eine Liste mit allen Kaffemaschinenobjekten:
    # coffee_Machines = myKitchen.getInteractiveAppliances("coffeeMachine")
    # coffee_Machines[0].brewing()

    # Man bekommt eine Liste mit allen Wasserkochern:
    # water_heaters = myKitchen.getInteractiveAppliances("waterHeater")
    # water_heaters[0].heating()

    # Man bekommt eine Liste mit allen Werkzeugen:
    # Tools = myKitchen.getTools()
    # for tool in Tools:
    #   print("Der Gegenstand " + tool.tool_id + " befindet sich in " + myKitchen.getLocationWithId(tool.tool_id))

