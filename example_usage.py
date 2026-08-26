from client import ModularNodeGraphDagLatentWorkflowExecutorClient

def main():
    client = ModularNodeGraphDagLatentWorkflowExecutorClient()
    res = client.execute_latent_node_dag('{"workflow": "AnimateDiff_IPAdapter_ControlNet_Flow"}')
    print('DAG Execution: ' + res['dag_execution_id'] + ' (' + str(res['nodes_evaluated_count']) + ' nodes evaluated)')
    print('VRAM Peak: ' + str(res['vram_peak_allocation_gb']) + ' GB | Latents Cached: ' + str(res['intermediate_latents_cached']))
    print('Execution Time: ' + str(res['topological_execution_time_seconds']) + 's')
    for u in res['output_artifacts_urls']:
        print('  - ' + u)

if __name__ == '__main__':
    main()
