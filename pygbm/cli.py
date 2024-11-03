import argparse
import matplotlib.pyplot as plt
from pygbm.gbm_simulator import GBMSimulator

def simulate_gbm(args):
    simulator = GBMSimulator(args.y0, args.mu, args.sigma)
    t_values, y_values = simulator.simulate_path(args.T, args.N)
    
    plt.plot(t_values, y_values, label="GBM Path")
    plt.xlabel("Time")
    plt.ylabel("Y(t)")
    plt.title("Simulated Geometric Brownian Motion Path")
    plt.legend()
    
    if args.output:
        plt.savefig(args.output)
    else:
        plt.show()

def main():
    parser = argparse.ArgumentParser(description="Simulate Geometric Brownian Motion.")
    subparsers = parser.add_subparsers(dest="command")

    simulate_parser = subparsers.add_parser("simulate", help="Simulate a Geometric Brownian Motion path.")
    simulate_parser.add_argument('--y0', type=float, required=True, help="Initial value Y(0)")
    simulate_parser.add_argument('--mu', type=float, required=True, help="Drift coefficient")
    simulate_parser.add_argument('--sigma', type=float, required=True, help="Diffusion coefficient")
    simulate_parser.add_argument('--T', type=float, required=True, help="Total time")
    simulate_parser.add_argument('--N', type=int, required=True, help="Number of steps")
    simulate_parser.add_argument('--output', type=str, help="Output file for the plot")
    simulate_parser.set_defaults(func=simulate_gbm)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
