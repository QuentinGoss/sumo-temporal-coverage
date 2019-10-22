# options.py
# Author: Quentin Goss
# The options parser options are here
import optparse
import env

def get_options():
    opt_parser = optparse.OptionParser()
    # GUI
    opt_parser.add_option("--nogui",action="store_true",default=False, help="run the commandline version of sumo")
    #
    opt_parser.add_option('--seed',type='int',dest='seed',default=8635839050,help='Random Seed')
    opt_parser.add_option('--map-dir',type='string',dest='map_dir',default=None,help='Directory of SUMO map files')
    #
    opt_parser.add_option('--targets',type='string',dest='targets',default=None,help='Targets file. Should contain one node id per line.')
    #
    opt_parser.add_option('--veh.total',type='int',dest='veh_total',default=1000,help='Total amount of vehicles.')
    opt_parser.add_option('--veh.exists.max',type='int',dest='veh_exists_max',default=50,help='The amount of vehicles that exist in the simulation at any time.')
    #
    opt_parser.add_option('--point.spawn',type='string',dest='point_spawn',default=None,help='The point where vehicles spawn around x.xx,y.yy.')
    opt_parser.add_option('--point.sink',type='string',dest='point_sink',default=None,help='The point where vehicles sink around x.xx,y.yy.')
    opt_parser.add_option('--radius.spawn.sink',type=int,dest='radius_spawn_sink',default=1000,help='The radius around the spawn and sink points where vehicles may spawn.')
    #
    opt_parser.add_option('-o','--out.dir',type='string',dest='out_dir',default='out',help='Output directory.')
    #
    options, args = opt_parser.parse_args()

    # Validate Options
    if options.map_dir == None:
        print('Please specify a map directory with --map-dir')
        sys.exit(1)
    elif options.targets == None:
        print("Please specify a targets file with --targets.")
        sys.exit(1)
    elif options.point_spawn == None:
        print("Please specify a spawn point with --point.spawn=x.xx,y.yy.")
        sys.exit(1)
    elif options.point_sink == None:
        print("Please specify a sink point with --point.spawn=x.xx,y.yy.")
        sys.exit(1)
        
    # Set variables
    env.veh_total = options.veh_total
    env.veh_exists_max = options.veh_exists_max
    env.point_spawn = parse_point(options.point_spawn)
    env.point_sink = parse_point(options.point_sink)
    env.radius_spawn_sink = options.radius_spawn_sink
    env.out_dir = options.out_dir

    return options

# For parsing spawn and sink points
def parse_point(point):
    point = point.strip('()').split(',')
    return (float(point[0]),float(point[1]))
