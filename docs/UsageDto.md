# UsageDto

## Properties
| Name                     | Type                                                    | Description | Notes      |
| ------------------------ | ------------------------------------------------------- | ----------- | ---------- |
| **count**                | **int**                                                 |             | [optional] |
| **daily_usage**          | [**list[DailyDto]**](DailyDto.md)                       |             | [optional] |
| **daily_volume_mb**      | **int**                                                 |             | [optional] |
| **end**                  | **datetime**                                            |             | [optional] |
| **failed_count**         | **int**                                                 |             | [optional] |
| **limit_change_events**  | [**list[LimitChangeEventDTO]**](LimitChangeEventDTO.md) |             | [optional] |
| **max_allowed_mb**       | **int**                                                 |             | [optional] |
| **max_limit_mb**         | **int**                                                 |             | [optional] |
| **start**                | **datetime**                                            |             | [optional] |
| **volume**               | **int**                                                 |             | [optional] |
| **volume_change_events** | [**list[LimitChangeEventDTO]**](LimitChangeEventDTO.md) |             | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
